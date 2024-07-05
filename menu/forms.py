from django import forms
from .models import Coffee, Snack

class OrderForm(forms.ModelForm):
    coffees = forms.ModelMultipleChoiceField(queryset=Coffee.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    snacks = forms.ModelMultipleChoiceField(queryset=Snack.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    # class Meta:
    #     model = Order
    #     fields = ['name', 'email', 'coffees', 'snacks']

