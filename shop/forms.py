from django import forms

from .models import Category, Product

class CateaForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug',)

class ProaForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','category','slug','image','description','price','stock',)

        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }