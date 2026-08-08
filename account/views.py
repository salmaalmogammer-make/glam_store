from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from products.models import Product, Category
from .models import User

# 1. صفحة الزوار الهبوط قبل تسجيل الدخول
def landing_index(request):
    return render(request, 'account/index.html')


# 2. دالة تسجيل الدخول (Login View)
def login_view(request):
    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        
        user = authenticate(request, username=username_input, password=password_input)
        
        if user is not None:
            login(request, user)
            
            # إذا كان أدمن ينقله للوحة التحكم، وإذا كانت عميلة تنقل لصفحة المنتجات
            if user.role == 'admin' or user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('client_home')
        else:
            return render(request, 'account/login.html', {'error': 'اسم المستخدم أو كلمة المرور غير صحيحة!'})
            
    return render(request, 'account/login.html')


# 3. دالة الصفحة الرئيسية للعملاء (تصفية المنتجات والأقسام)
def client_home(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        selected_category = Category.objects.filter(id=category_id).first()
    else:
        products = Product.objects.all()
        selected_category = None
        
    return render(request, 'account/home.html', {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
    })


# 4. دالة عرض صفحة تفاصيل المنتج المنفصلة
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})


# 5. دالة إنشاء حساب جديد (تُحفظ في قاعدة البيانات وتسمح بالدخول فوراً)
def register_client(request):
    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        skin_type_input = request.POST.get('skin_type')
        phone_input = request.POST.get('phone')
        
        if User.objects.filter(username=username_input).exists():
            return render(request, 'account/register.html', {
                'error': 'اسم المستخدم هذا مستخدم بالفعل، يرجى اختيار اسم آخر!'
            })
        
        # إنشاء الحساب وحفظه في قاعدة البيانات كحساب مفعّل جاهز للدخول
        user = User.objects.create_user(
            username=username_input,
            password=password_input,
            skin_type=skin_type_input,
            phone=phone_input,
            role='client',
            is_active=True  # مفعّل فوراً لينزل بقاعدة البيانات ويقدر يدخل مباشرة
        )
        
        # تسجيل الدخول التلقائي وتحويل العميلة لصفحة المنتجات فوراً
        login(request, user)
        return redirect('client_home')
        
    return render(request, 'account/register.html')