from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import forlo
from django.views.generic import CreateView,ListView, UpdateView, DeleteView
from .forms import forusuc
from .models import usuario
from django.shortcuts import render, redirect
from django.contrib import messages

class Login(FormView):
    template_name = 'login.html'
    form_class = forlo
    success_url = reverse_lazy('shop:home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())

        else:
            #return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            #messages.error(request, 'Por favor, introduzca un Nombre de Usuario y clave correctos. Observe que ambos campos pueden ser sensibles a mayúsculas')
            return super(Login,self).dispatch(request,*args, **kwargs)

        
    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutu(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class lisus(ListView):
    model = usuario
    template_name = 'usuarios.html'
    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
    #queryset = usuario.objects.all()

class resus(CreateView):
    model = usuario
    form_class = forusuc
    template_name = 'agus.html'
    success_url = reverse_lazy('usuarios:listaus')

def elius(request, pk):
    if request.method == 'POST':
        elu = usuario.objects.get(pk=pk)
        elu.delete()
    return redirect('usuarios:listaus')

def idp(request, pk):
    if request.method == 'POST':
        elu = usuario.objects.get(pk=pk)
    return (elu)

def usu_eli(request, pk):
    elisu = usuario.objects.get(pk=pk)
    if request.method == 'POST':
        elisu.delete()
        return redirect('usuarios:listaus')
    return render(request, 'elus.html', {'usu':elisu})


class used(UpdateView):
    model = usuario
    form_class = forusuc
    template_name = 'edus.html'
    success_url = reverse_lazy('usuarios:listaus')

# view para recuperar contra

def mesaje(request):

    return render(request, "contra/men.html")
