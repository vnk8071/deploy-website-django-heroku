from django.urls import path
from .models import Post
from django.views.generic import ListView, DetailView
from . import views
urlpatterns = [
    path('', ListView.as_view(
        queryset = Post.objects.all().order_by('-date_posted'),
        template_name = 'blog/blog.html',
        context_object_name = 'Posts',
        paginate_by = 3), name= 'blog'),
    
    path('<int:pk>', views.post,
        name= 'post'),
]