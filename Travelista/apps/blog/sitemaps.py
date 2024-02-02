# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse

from apps.blog.models import Post


class BlogSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.posts.showable()

    def lastmod(self, post):
        return post.published_date

    def location(self, post):
        return reverse('blog:single', args=[
            post.id,
        ])
