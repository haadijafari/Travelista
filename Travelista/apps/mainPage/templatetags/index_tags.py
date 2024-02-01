from django import template
from apps.blog.models import Post

register = template.Library()

@register.inclusion_tag('Travelista/index/index-blog-area.html')
def latest_posts(arg=6):
    posts = Post.posts.showable()[:arg]
    return {'latest_posts': posts}