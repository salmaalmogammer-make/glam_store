from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_client, name='register'), # مسار تسجيل العملاء
    path('home/', views.client_home, name='client_home'),
    path('', views.landing_index, name='landing_index'),
]