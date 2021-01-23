from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

class EdoForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['paid',]
        widgets = {
            'paid': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

        
