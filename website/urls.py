from re import template
from django.urls import path
from . import views
from .models import Project
from django.contrib.auth import views as auth_views
from django.views.generic import ListView
urlpatterns = [
    path('', views.index, name= 'website'),
    path('contact/', views.contact, name= 'contact'),
    path('register/', views.register, name= 'register'),
    path('login/', auth_views.LoginView.as_view(template_name="pages/login.html"), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'pages/website.html'), name= 'logout'),
    path('project/', ListView.as_view(
        queryset = Project.objects.all(),
        template_name = 'pages/project.html',
        context_object_name = 'Projects'), name= 'project')
]