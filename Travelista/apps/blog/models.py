from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager


class PostManager(models.Manager):
    def showable(self):
        current_datetime = timezone.now()
        posts = self.filter(Q(status=1) &
                            Q(published_date__lt=current_datetime)).order_by('-published_date')
        return posts

class Category(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = _('Draft')
        PUBLISHED = _('Published')

    img = models.ImageField(_('Image'), upload_to='', default='blog_media/default.jpg')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), max_length=255, allow_unicode=True, unique_for_date='published_date')
    content = models.TextField(_('Content'), )
    tag = TaggableManager(_('Tag'), blank=True)
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(_('Counted Views'), default=0)
    # status = models.CharField(_('Status'), default=StatusChoices.DRAFT, max_length=15, null=False, choices=StatusChoices.choices)
    status = models.BooleanField(_('Status'), default=False)
    published_date = models.DateTimeField(_('Publish Date'), null=True, blank=True)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date'), auto_now=True)

    posts = PostManager()
    objects = models.Manager()

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-published_date',)

    def __str__(self) -> str:
        return self.title
