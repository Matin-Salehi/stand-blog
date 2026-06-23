from django.shortcuts import render, get_object_or_404, redirect
import blog_app
from blog_app.models import Post, Category


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog_app/post-details.html', {'post': post})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/blog.html', {'posts': posts})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all()
    return render(request, 'blog_app/blog.html', {'posts': posts})