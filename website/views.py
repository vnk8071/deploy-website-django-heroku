from django.shortcuts import render
from .form import RegistrationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from website.models import Project

# Create your views here.
def index(request):
    return render(request, 'pages/website.html')

def contact(request):
    return render(request, 'pages/contact.html')

def error(request):
    return render(request, 'pages/error.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})

def project(request):
    project = get_object_or_404(Project)
    if request.method == 'POST':
        return HttpResponseRedirect(request.path)
    return render(request, 'pages/project.html', {'project':project})
