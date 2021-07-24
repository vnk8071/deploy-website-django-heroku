from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_posted']
    list_filter = ['date_posted']
    search_fields = ['title']
    inlines = [CommentInline]
admin.site.register(Post, PostAdmin)