from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import HomePost
from .forms import PostForm
from django.shortcuts import redirect

def main_home(request):
    return render(request, 'home/index.html')