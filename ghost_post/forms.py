from django import forms
from .models import Post


class AddPost(forms.Form):
    CHOICES = [(True, 'roast'), (False, 'boast')]
    content = forms.CharField(max_length=255)
    is_roast = forms.ChoiceField(choices=CHOICES)
