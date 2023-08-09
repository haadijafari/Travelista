from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/blog-popular-post.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-post-category.html')
def categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for cat in categories:
        cat_dict[cat] = posts.filter(category=cat).count()
    return {'categories': cat_dict}
