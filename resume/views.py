from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import ProfilePost
from .forms import PostForm
from django.shortcuts import redirect

def profile_home(request):
    post = get_object_or_404(ProfilePost, pk=1)
    return render(request, 'resume/index.html', {'post': post})