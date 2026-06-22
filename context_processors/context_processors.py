from blog_app.models import Post


def recent_posts(request):
    recent_posts = Post.objects.order_by('-created_at', 'updated_at')[:3]
    return {'recent_posts': recent_posts}