from django.contrib import admin

from .models import Blog, Category, Comment

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)