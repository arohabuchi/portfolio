from django.shortcuts import render
from .models import project
# Create your views here.
def projects(request):
    projects = project.objects.all()
    return render(request, 'project/index.html', locals())