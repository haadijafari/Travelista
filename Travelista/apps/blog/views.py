from django.shortcuts import render, get_object_or_404
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone   #This is for filtering by published_date
from .models import Post


def blog_home(request, **kwargs):
    posts = Post.posts.showable()
    if cat_name := kwargs.get('cat_name'):
        posts = posts.filter(category__name=cat_name)
    if author := kwargs.get('author'):
        posts = posts.filter(author__username=author)

    posts = Paginator(posts, 5)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    content = {'posts': posts}
    return render(request, 'blog/blog-home.html', content)


def blog_single(request, **kwargs):
    posts = Post.posts.showable()
    if pid := kwargs.get('pid'):
        post = posts.get(id=pid)
        post.counted_views += 1
        post.save()
        # post = get_object_or_404(posts, pk=pid)
    content = {'post': post, 'posts': posts }
    return render(request, 'blog/blog-single.html', content)


def blog_search(request):
    posts = Post.posts.showable()
    if request.method == 'GET':
        if s := request.GET.get('search'):
            posts = posts.filter(content__icontains=s)
            posts = chain(Post.objects.filter(title__icontains=s), posts)

    # posts = Paginator(posts,3)
    # try:
    #     page_number = request.GET.get('page')
    #     posts = posts.get_page(page_number)
    # except PageNotAnInteger:
    #     posts = posts.get_page(1)
    # except EmptyPage:
    #     posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
