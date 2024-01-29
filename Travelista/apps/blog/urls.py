from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_home, name='index'),
    path('single/<int:pid>', blog_single, name='single'),
    path('category/<str:cat_name>', blog_home, name='category'),
    path('author/<str:author>', blog_home, name='author'),
    path('search/',blog_search,name='search'),
]
