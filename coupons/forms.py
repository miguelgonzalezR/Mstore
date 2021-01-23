from django import forms

class CouponApplyForm(forms.Form):
    codigo = forms.CharField()
