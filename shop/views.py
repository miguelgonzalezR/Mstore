from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from .forms import CateaForm, ProaForm
from django.urls import reverse_lazy
from datetime import date
from datetime import datetime
from django.db.models.functions import Coalesce
from django.db.models import Sum
from orders.models import Order


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

# viwes para el sitio privado

def catlis(request):
    cate = Category.objects.all()
    return render(request, 'privado/category.html', {'cate': cate})

class agcate(CreateView):
    model = Category
    form_class = CateaForm
    template_name = 'privado/newcet.html'
    success_url = reverse_lazy('shop:Categorias')

class edca(UpdateView):
    model = Category
    form_class = CateaForm
    template_name = 'privado/updateca.html'
    success_url = reverse_lazy('shop:Categorias')

def elica(request, pk):
    if request.method == 'POST':
        cate = Category.objects.get(pk=pk)
        cate.delete()
    return redirect('shop:Categorias')

def idca(request, pk):
    if request.method == 'POST':
        cate = Category.objects.get(pk=pk)
    return (cate)

def cat_eli(request, pk):
    cate = Category.objects.get(pk=pk)
    if request.method == 'POST':
        cate.delete()
        return redirect('shop:Categorias')
    return render(request, 'privado/deleteca.html', {'cat':cate})

# views productos privado

def prolis(request):
    pro = Product.objects.all()
    return render(request, 'privado/productos/productos.html', {'prod': pro})

class agcpro(CreateView):
    model = Product
    form_class = ProaForm
    template_name = 'privado/productos/newpro.html'
    success_url = reverse_lazy('shop:Productos')

class edpro(UpdateView):
    model = Product
    form_class = ProaForm
    template_name = 'privado/productos/updatepro.html'
    success_url = reverse_lazy('shop:Productos')

def elipro(request, pk):
    if request.method == 'POST':
        pro = Product.objects.get(pk=pk)
        pro.delete()
    return redirect('shop:Productos')

def idpro(request, pk):
    if request.method == 'POST':
        pro = Product.objects.get(pk=pk)
    return (pro)

def pro_eli(request, pk):
    pro = Product.objects.get(pk=pk)
    if request.method == 'POST':
        pro.delete()
        return redirect('shop:Productos')
    return render(request, 'privado/productos/deletepro.html', {'prod':pro})

# graficos privados


class homeg(TemplateView):
    template_name ='privado/index.html'

    def fechag(self):
        datos = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                total = Order.objects.filter(created__year=year, created__month=m).aggregate(r=Coalesce(Sum('get_total_cost'), 0)).get('r')
                datos.append(float(total))
        except:
            pass
        return datos
        

    def graf(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grafico_1'] = self.fechag()
        return context

def graf(request):
    return render(request, 'privado/index.php')

#ayuda

def ayuda(request):
    return render(request, 'shop/ayuda.html')

#sobre nosotros
def nosob(request):
    return render(request, 'shop/sobreno.html')
