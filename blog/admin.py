from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','author', 'publish', 'status')

admin.site.register(Post)
