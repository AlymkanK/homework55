from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from webapp.models import Task
# Create your views here.

def index(request):
    tasks = Task.objects.order_by('-date')
    return render(request, 'index.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        date = request.POST.get('date')

        if description and status:
            task = Task(description=description, status=status, date=date)
            task.save()
            return redirect('index')
        else:
            return HttpResponse('')
    return render(request, 'add_task.html')