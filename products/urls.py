from django.urls import path
from account import views  # أو استدعاء الدالة من المكان الذي أضفتِ فيه product_detail

urlpatterns = [
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]