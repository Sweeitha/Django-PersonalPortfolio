from django.shortcuts import render, get_object_or_404
from .models import Blog
from .models import BlogProject

def bloghome(request):
    myblogs = Blog.objects.all()
    #mystudies = Myself.objects.order_by('-date')[:5]
    #displays first 5 items in order of date, if we add date as an attribute of myself
    return render(request, 'blog/home.html', {'myblogs':myblogs})

def blogprojects(request):
    blogs = BlogProject.objects.order_by('-date')[:5]
    return render(request, 'blog/projects.html', {'projects':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Myself, pk=blog_id)
    return render(request, 'blog/detail.html', {'Blog':blog})
