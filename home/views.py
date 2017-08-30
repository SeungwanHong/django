from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import HomePost
from .forms import PostForm
from django.shortcuts import redirect

def main_home(request):
    post = get_object_or_404(HomePost, pk=1)
    return render(request, 'home/index.html', {'post': post})