from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'مديرة المتجر / مشرف'),
        ('client', 'عميلة / زبونة'),
    )
    
    SKIN_TYPE_CHOICES = (
        ('dry', 'جافة'),
        ('oily', 'دهنية'),
        ('combination', 'مختلطة'),
        ('normal', 'عادية'),
        ('sensitive', 'حساسة'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client', verbose_name="نوع المستخدم")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="رقم الهاتف")
    address = models.TextField(blank=True, null=True, verbose_name="العنوان")
    skin_type = models.CharField(max_length=20, choices=SKIN_TYPE_CHOICES, blank=True, null=True, verbose_name="نوع البشرة")

    def save(self, *args, **kwargs):
        # إذا كان الحساب هو حسابكِ الرئيسي (الـ Superuser الوحيد) يصبح الأدمن
        if self.is_superuser:
            self.role = 'admin'
        else:
            # جميع المستخدمين والمسجلين الجدد يدخلون كعملاء فوراً
            self.role = 'client'
            self.is_staff = False
            self.is_superuser = False
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - ({self.get_role_display()})"