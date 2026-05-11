from django.urls import path
from . import views

urlpatterns = [
    # 🏠 Home page (product list)
    path('', views.home, name='home'),

    # 📦 Product detail page
    path('product/<int:pk>/', views.product_detail, name='product'),

    # 🛒 Cart page
    path('cart/', views.cart, name='cart'),

    # ➕ Add to cart
    path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),

    # 👤 Register page
    path('register/', views.register, name='register'),

    # 🧾 Checkout page
    path('checkout/', views.checkout, name='checkout'),
]