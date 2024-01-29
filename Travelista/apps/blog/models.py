from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PostManager(models.Manager):
    def showable(self):
        current_datetime = timezone.now()  # This is for filtering by published_date
        posts = self.filter(published_date__lt=current_datetime)  # This is for filtering by published_date
        posts = posts.filter(status=1).order_by('-published_date')
        return posts

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    img = models.ImageField(upload_to='', default='blog_media/default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    posts = PostManager()
    objects = models.Manager()

    class Meta:
        ordering = ('-created_date',)

    def __str__(self) -> str:
        return self.title
