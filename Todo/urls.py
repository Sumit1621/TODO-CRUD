<<<<<<< HEAD
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
]


=======
from django.urls import path
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_task, name='add_task'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle_task'),
    
]
>>>>>>> 5627e246f8bcf8967020b36f2ba8986b86cf8203
