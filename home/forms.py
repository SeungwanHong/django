from django import forms

from .models import HomePost

class PostForm(forms.ModelForm):

    class Meta:
        model = HomePost
        fields = ()