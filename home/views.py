from multiprocessing import context
from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect
from home.models import Task
# Create your views here.

def home(request):
    context={'success': False}
    if request.method=="POST":
        tittle=request.POST['tittle']
        desc=request.POST['desc']
        print(tittle,desc)
        ins=Task(taskTittle=tittle, taskDesc=desc)
        ins.save()
        context={'success': True}

    
    return render(request, 'index.html',context)

def task(request):
    allTasks=Task.objects.all()
    context={'tasks': allTasks}
    return render(request, 'task.html', context)