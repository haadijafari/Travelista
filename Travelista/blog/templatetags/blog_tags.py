from django import template
from blog.models import Post, Category
from datetime import datetime   #This is for filtering by published_date


register = template.Library()

@register.inclusion_tag('blog/blog-popular-post.html')
def latest_posts(arg=3):
    current_datetime = datetime.now()    #This is for filtering by published_date
    posts = Post.objects.filter(published_date__lt=current_datetime)     #This is for filtering by published_date
    posts = posts.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-post-category.html')
def categories():
    current_datetime = datetime.now()    #This is for filtering by published_date
    posts = Post.objects.filter(published_date__lt=current_datetime)     #This is for filtering by published_date
    posts = posts.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for cat in categories:
        cat_dict[cat] = posts.filter(category=cat).count()
    return {'categories': cat_dict}


@register.filter
def get_by_id(lst, post_id):
    return next((post for post in lst if post.id == post_id), None)
