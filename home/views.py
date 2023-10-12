from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskUpdateForm

from home.models import Task

# Create your views here.
def home(request):
    # Initialize context dictionary
    context = {'success' : False}

    # Check if request method is POST
    if request.method == "POST":
        # Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)

        # Create a new Task instance
        ins = Task(task_title=title, task_description=desc)

        # Save the Task instance to the database
        ins.save()

        # Update context dictionary
        context = {'success' : True}

    # Render the index.html template with the context dictionary
    return render(request, 'index.html', context)


def tasks(request):
    allTasks =Task.objects.all()
    context = {'tasks' : allTasks}
    #print(allTasks)
    return render(request, 'tasks.html', context)
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskUpdateForm(instance=task)
    
    return render(request, 'update_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    
    return render(request, 'delete_task.html', {'task': task})


