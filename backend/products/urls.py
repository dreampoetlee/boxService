from django.urls import path, include
from products import views

urlpatterns = [
  path('', views.product_list),
  path('<int:pk>/', views.product_detail)
]