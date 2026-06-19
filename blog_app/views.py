from django.shortcuts import render

from blog_app.models import Post


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog_app/post-details.html', {'post': post})