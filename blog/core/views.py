from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-date_published')
    data = {
        'post_list': posts,
    }
    return render(request, 'core/index.html', data)

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    data = {
        'post': post
    }
    return render(request, 'core/detail.html', data)

def about(request):
    return render(request, 'core/about.html')
