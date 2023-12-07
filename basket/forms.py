from django import forms


class BasketAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=20)
