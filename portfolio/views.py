from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def home(request):
    Projectsoutthere = Project.objects.all()
    #to use all the projects(Objects) we created in db through class of models
    return render(request, 'Homepage/Home.html', {'Projects':Projectsoutthere})
    #make the returned value as a dict value so that key can be used in html
