from django import forms
from django.db.models.query import QuerySet
from produto.models import SaborPizza

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 8)]

class CartAddProductForm(forms.Form):
  quantidade = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
  update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)

class CartAddPizzaDoisSaboresForm(forms.Form):
  primeiro_sabor = forms.ModelChoiceField(queryset=SaborPizza.objects.all(), to_field_name="sabor")
  segundo_sabor = forms.ModelChoiceField(queryset=SaborPizza.objects.all(), to_field_name="sabor")
  quantidade = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
