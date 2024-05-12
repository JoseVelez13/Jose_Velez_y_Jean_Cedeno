from django.shortcuts import render
from .models import Project
from django.shortcuts import redirect

# Create your views here.
def home(request):
    projects=Project.objects.all()
    return render(request,'home.html'
                  ,{'projects': projects})

def blog_1(request):
    return render(request, 'blog/1.html')

def blog_2(request):
    return render(request, 'blog/2.html')

