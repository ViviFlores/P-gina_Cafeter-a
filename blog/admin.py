from django.contrib import admin
from .models import Category, Blog

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Category, CategoryAdmin)


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=('title', 'author', 'published')
    ordering=('author','published')
    search_fields=('title',)
    date_hierarchy='published'
    list_filter=('author','categories__name')   #'author__username'

admin.site.register(Blog, BlogAdmin)
