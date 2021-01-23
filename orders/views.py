from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import OrderItem, Order
from .forms import OrderCreateForm, EdoForm
from cart.cart import Cart
from .utils import order_created
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            #send mail
            order_created(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:   
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

@staff_member_required
def readdo(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/readod.html', {'order': order})

def redpd(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/deop.html', {'order': order})


def prolis(request):
    orde = Order.objects.all()
    return render(request, 'admin/orders/order/orders.html', {'order': orde})

class edor(UpdateView):
    model = Order
    form_class = EdoForm
    template_name = 'admin/orders/order/updateor.html'
    success_url = reverse_lazy('orders:Ordenes')



