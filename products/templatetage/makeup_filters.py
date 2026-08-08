from django import template

register = template.Library()

# 1. فلتر لتنسيق السعر وإضافة العملة
@register.filter(name='currency')
def currency(value):
    try:
        return f"{float(value):,.2f} ر.س"
    except (ValueError, TypeError):
        return value

# 2. فلتر لتنسيق نوع البشرة بالعربي
@register.filter(name='skin_type_ar')
def skin_type_ar(value):
    skin_map = {
        'dry': 'جافة',
        'oily': 'دهنية',
        'combination': 'مختلطة',
        'normal': 'عادية',
        'sensitive': 'حساسة',
        'all': 'جميع أنواع البشرة'
    }
    return skin_map.get(value, value)