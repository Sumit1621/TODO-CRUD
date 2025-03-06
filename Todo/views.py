from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm
from django.views.decorators.csrf import csrf_exempt

def home(request):
    form = TodoForm()
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos, 'form': form})

@csrf_exempt
def add_task(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.save()
            return JsonResponse({
                'id': task.id,
                'title': task.title,
                'priority': task.priority,
                'completed': task.completed
            })
    return JsonResponse({'error': 'Invalid data'}, status=400)

@csrf_exempt
def toggle_task(request, task_id):
    try:
        task = Todo.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
        return JsonResponse({'completed': task.completed})
    except Todo.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)







