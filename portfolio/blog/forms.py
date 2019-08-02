from django import forms
from .models import Post
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Layout, Submit

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    text = forms.CharField(widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
           'title',
           'text',
           Submit('submit', 'Add')
        )
    class Meta:
        model = Post
        fields = ['title', 'text',]
