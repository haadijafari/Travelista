from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_home, name='index'),
    path('single/<int:pid>', blog_single, name='single'),
]
