from django.contrib import admin
from . models import Post, Comment, Document

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_date', 'published_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Document)
