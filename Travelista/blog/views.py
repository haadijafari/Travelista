from django.shortcuts import render, get_object_or_404
from blog.models import Post
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime   #This is for filtering by published_date


def blog_home(request, **kwargs):
    current_datetime = datetime.now()    #This is for filtering by published_date
    posts = Post.objects.filter(published_date__lt=current_datetime)     #This is for filtering by published_date
    posts = posts.filter(status=1).order_by('-published_date')
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
    posts = Post.objects.filter(status=1)
    if pid := kwargs.get('pid'):
        post = posts.get(id=pid)
        post.counted_views += 1
        post.save()
        # post = get_object_or_404(posts, pk=pid)
    content = {'post': post, 'all_posts': posts }
    return render(request, 'blog/blog-single.html', content)


def blog_search(request):
    posts = Post.objects.filter(status=1)
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
