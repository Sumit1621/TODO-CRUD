from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
    
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos, 'form': form})







