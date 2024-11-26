from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Cart
from products.models import Products
from django.contrib.auth.decorators import login_required
from e_commerce.settings import LOGIN_URL
from django.shortcuts import get_object_or_404
from login.models import UserProfile
# Create your views here.


class CartView(ListView):
    template_name='Cart/cart.html'
    model=Cart
    context_object_name='cart'

@login_required(login_url=LOGIN_URL)
def remove_from_cart(request,product_id):
    cart_item=Cart.objects.get(id=product_id)
    cart_item.delete()
    return redirect ('cart:cart')

@login_required(login_url=LOGIN_URL)
def add_to_cart(request,product_id):
    product=Products.objects.get(product_id=product_id)
    user=get_object_or_404(UserProfile,user=request.user)
    cart_item,created=Cart.objects.get_or_create(product=product,user=user)
    return redirect('cart:cart')
    