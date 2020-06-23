from django.contrib import admin

# for internal application import

from .models import Post

# Register your models here.

admin.site.register(Post)