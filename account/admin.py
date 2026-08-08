from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# تسجيل نموذج المستخدم المخصص لمتجر الميكأب في لوحة التحكم
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # إظهار الحقول المخصصة (نوع المستخدم، الهاتف، نوع البشرة) في لوحة التحكم
    fieldsets = UserAdmin.fieldsets + (
        ('معلومات متجر التجميل المخصصة', {'fields': ('role', 'phone', 'address', 'skin_type')}),
    )
    
    # عرض الحقول في الجدول بما فيها حقل التفعيل is_active
    list_display = ('username', 'email', 'role', 'skin_type', 'is_active', 'is_staff')
    
    # إضافة الفلترة حسب الحالة ونوع المستخدم
    list_filter = ('role', 'is_active', 'skin_type', 'is_staff')
    
    # تفعيل خيار الموافقة بضغطة زر من القائمة الرئيسية مباشرة
    list_editable = ('is_active',)