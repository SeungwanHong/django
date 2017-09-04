from django import forms

from .models import ProfilePost

class PostForm(forms.ModelForm):

    class Meta:
        model = ProfilePost
        fields = ()