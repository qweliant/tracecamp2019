from django import forms
from .models import Grocery
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Layout, Submit

class GroceryCreateForm(forms.ModelForm):
    item = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Grocery'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Category'}))
    in_stock = forms.BooleanField(required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
           'item',
           'category',
           'in_stock',
           Submit('submit', 'Add')
        )
    class Meta:
        model = Grocery
        fields = ['item', 'category', 'in_stock',]
