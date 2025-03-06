from django.urls import path
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_task, name='add_task'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle_task'),
    
]