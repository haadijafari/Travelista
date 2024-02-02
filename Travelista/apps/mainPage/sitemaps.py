# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse

class MainPageViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = "daily"
    protocol = 'https'

    def items(self):
        return ["index:Travelista", "index:about", "index:contact", "blog:index"]

    def location(self, item):
        return reverse(item)
