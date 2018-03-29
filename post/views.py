from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def post_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/posts.html', context)

def post_detail(request, kimlik):
    post = get_object_or_404(Post, id=kimlik)
    context = {
        'post': post
    }
    return render(request, 'post/detail.html', context)

def post_create(request):
    return HttpResponse("Burası Post Create Sayfası")

def post_update(request):
    return HttpResponse("Burası Post Update Sayfası")

def post_delete(request):
    return HttpResponse("Burası Post Delete Sayfası")
