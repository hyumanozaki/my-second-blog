from django.shortcuts import render
from django.utils import timezone
from .models import Post
#from .models import MBO22,ADC22,ADC22RH,PDI22#, PDI22G
#from .models import MBO
from .forms import PostForm
#from .forms import MBO22AForm,MBO22Q1Form,MBO22Q2Form,MBO22Q3Form,MBO22Q4Form,ADC22CForm,ADC22AOForm,PDI22Form#PDI22GForm,PDI22EForm,PDI22GCForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import TemplateView #テンプレートタグ
#from .forms import AccountForm#, AddAccountForm #ユーザーアカウントフォー
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
#from django.core.mail import send_mail
from datetime import datetime
import numpy as np
import pandas as pd


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})