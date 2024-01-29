from django import template
from apps.blog.models import Post, Category

register = template.Library()


@register.inclusion_tag('blog/blog-popular-post.html')
def latest_posts(arg=3):
    posts = Post.posts.showable()[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-category.html')
def categories():
    posts = Post.posts.showable()
    categories = Category.objects.all()
    cat_dict = {}
    for cat in categories:
        cat_dict[cat] = posts.filter(category=cat).count()
    return {'categories': cat_dict}


@register.filter(name='get_previous_post')
def get_previous_post(post, posts):
    previous_post = None
    for p in posts:
        if p.published_date < post.published_date and (not previous_post or p.published_date > previous_post.published_date):
            previous_post = p
    return previous_post


@register.filter(name='get_next_post')
def get_next_post(post, posts):
    next_post = None
    for p in posts:
        if p.published_date > post.published_date and (not next_post or p.published_date < next_post.published_date):
            next_post = p
    return next_post

