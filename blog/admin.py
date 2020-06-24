from django.contrib import admin

# for internal application import

from .models import Post

# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish','status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = { 'slug': ('title',) }
    date_hierarchy = 'publish'
    raw_id_fields = ('author',)
    ordering = ('status','publish')
