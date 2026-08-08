from django.db import models

# 1. نموذج الفئات والأقسام
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم القسم")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="الرابط اللطيف (Slug)")
    description = models.TextField(blank=True, null=True, verbose_name="وصف القسم")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="صورة القسم")

    class Meta:
        verbose_name = "قسم"
        verbose_name_plural = "الأقسام"

    def __str__(self):
        return self.name


# 2. نموذج الماركات / البراندات
class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الماركة")
    logo = models.ImageField(upload_to='brands/', blank=True, null=True, verbose_name="شعار الماركة")

    class Meta:
        verbose_name = "ماركة"
        verbose_name_plural = "الماركات"

    def __str__(self):
        return self.name


# 3. نموذج المنتجات الرئيسي
class Product(models.Model):
    SKIN_TYPE_CHOICES = (
        ('all', 'جميع أنواع البشرة'),
        ('dry', 'البشرة الجافة'),
        ('oily', 'البشرة الدهنية'),
        ('combination', 'البشرة المختلطة'),
        ('normal', 'البشرة العادية'),
        ('sensitive', 'البشرة الحساسة'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="القسم")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name="الماركة")
    name = models.CharField(max_length=150, verbose_name="اسم المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر الأساسي")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="السعر بعد الخصم")
    description = models.TextField(verbose_name="وصف المنتج وطريقة الاستخدام")
    
    # خيار رفع الصورة من الملفات + خيار رابط الصورة
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="صورة المنتج (من الجهاز)")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="رابط الصورة (من الإنترنت)")

    suitable_skin_type = models.CharField(max_length=20, choices=SKIN_TYPE_CHOICES, default='all', verbose_name="مناسب لنوع البشرة")
    is_available = models.BooleanField(default=True, verbose_name="متوفر في المخزون")
    is_featured = models.BooleanField(default=False, verbose_name="منتج مميز (يظهر بالرئيسية)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name


# 4. نموذج درجات وألوان الميكأب
class ProductShade(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='shades', verbose_name="المنتج")
    shade_name = models.CharField(max_length=100, verbose_name="اسم الدرجة / اللون")
    color_code = models.CharField(max_length=7, blank=True, null=True, verbose_name="كود اللون Hex (مثال: #FF5733)")
    shade_image = models.ImageField(upload_to='products/shades/', blank=True, null=True, verbose_name="صورة الدرجة")
    stock = models.PositiveIntegerField(default=0, verbose_name="الكمية المتوفرة")

    class Meta:
        verbose_name = "درجة / لون"
        verbose_name_plural = "درجات الألوان"

    def __str__(self):
        return f"{self.product.name} - {self.shade_name}"