from django.contrib import admin
from .models import Product, Category, Brand

# 1. تخصيص طريقة عرض المنتجات
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # استخدام الحقول الأساسية الموجودة مؤكداً في الموديل
    list_display = ('name', 'price', 'suitable_skin_type')
    list_filter = ('suitable_skin_type', 'category', 'brand')
    search_fields = ('name',)

# 2. تسجيل الأقسام والماركات
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)