from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    list_display = ('title', 'status', 'counted_views', 'published_date', )
    list_filter = ('status', 'published_date', )
    # ordering = ('-published_date', )
    search_fields = ('title', 'content', )
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', )
    list_filter = ('active', )
    # ordering = ('name', )
    search_fields = ('name',)