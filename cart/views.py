from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm
from django.contrib import messages
from django.http import HttpResponseRedirect

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        cd = form.cleaned_data
        if product.stock >= quantity:
            cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        else:
             messages.error(request, 'Lamentablemente la cantidad que usted nos a solicitado de este producto supera nuestro stock')
             return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        return redirect('cart:cart_detail')
    

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'update': True
        })
    coupon_apply_form = CouponApplyForm()
    return render(request, 'cart/detail.html', {'cart': cart, 'coupon_apply_form': coupon_apply_form})
