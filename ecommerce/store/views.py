from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Product, Order, OrderItem


# 🏠 Home page (product list)
def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


# 📦 Product detail page
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'store/product.html', {'product': product})


# 🛒 Add to cart
@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk)

    order, created = Order.objects.get_or_create(
        user=request.user,
        completed=False
    )

    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        product=product
    )

    order_item.quantity += 1
    order_item.save()

    return redirect('cart')


# 🛒 Cart page
@login_required
def cart(request):
    order = Order.objects.filter(user=request.user, completed=False).first()

    items = []
    total = 0

    if order:
        items = OrderItem.objects.filter(order=order)
        for item in items:
            total += item.product.price * item.quantity

    return render(request, 'store/cart.html', {
        'items': items,
        'total': total
    })


# 🧾 Checkout
@login_required
def checkout(request):
    order = Order.objects.filter(user=request.user, completed=False).first()

    if order:
        order.completed = True
        order.save()

    return redirect('home')


# 👤 Register (Signup)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'store/register.html', {'form': form})