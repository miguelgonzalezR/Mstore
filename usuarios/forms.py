from django import forms
from django.contrib.auth.forms import AuthenticationForm
from usuarios.models import usuario

class forlo (AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(forlo, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class forusuc(forms.ModelForm):

    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder':'Ingrese una contraseña',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label= 'Contraseña de comfirmacion', widget= forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder':'Verifique su Contraseña',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = usuario
        fields = ('email', 'username', 'nombres', 'apellidos')
        admin = [False, True]
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electronico'
                }
            ),

            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre'
                }
            ),

            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido'
                }
            ),

            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre de usuario'
                }
            ),

        }



         

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Las contraseña no son iguales')
        return password2

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])


        
        user.save()

        if commit:
            user.save()
        return user