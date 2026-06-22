from django.shortcuts import render

from blog_app.models import Post


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog_app/post-details.html', {'post': post})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/blog.html', {'posts': posts})