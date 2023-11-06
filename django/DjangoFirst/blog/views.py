from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.shortcuts import render

def create_post(request):
    if request.method == 'GET':
        context = {
            'form':PostForm()
        }
        return render(request, 'blog/post_form.html', context)

def home(request):

    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Zen of Python'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
