from django.contrib import admin
from mainPage.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = [
        'name',
        'subject',
        'email',
        'created_date',
        'updated_date',
    ]
    search_fields = ('name', 'email', 'subject', )
