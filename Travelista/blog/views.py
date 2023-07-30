from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_home(request):
    posts = Post.objects.filter(status=1)
    content = {'posts': posts}
    return render(request, 'blog/blog-home.html', content)

def blog_single(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if pid := kwargs.get('pid'):
        post = posts.get(id=pid)
        # post = get_object_or_404(posts, pk=pid)
    content = {'post': post}
    return render(request, 'blog/blog-single.html', content)
