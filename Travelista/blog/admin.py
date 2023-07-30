from django.contrib import admin
from blog.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title', 'status', 'counted_views',
                    'published_date', 'created_date', )
    list_filter = ('status', )
    ordering = ('-created_date', )
    search_fields = ('title', 'content', )

admin.site.register(Category)