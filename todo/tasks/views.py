
from django.shortcuts import redirect, render
from .models import *
from .forms import *


# Create your views here.
def index(request):

#getting objects from the database and form
    tasks = Task.objects.order_by('-time_added')

    form = TaskForm() 

#saving items to the database
    if request.method == 'POST':       
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'tasks': tasks, 'form': form }
    return render(request, 'tasks/index.html', context)



#this is for getting each items using a primary key
def update_task(request, pk ):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

#updating and saving each items, 
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task )
        if form.is_valid():
            form.save()
        return redirect('/')
        
           
    context = {'form':form}
    return render(request,'tasks/update_task.html', context )



#this is the view function for deleting a task
def deleteTask(request,pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task':task }
    return render(request, 'tasks/delete_task.html', context )