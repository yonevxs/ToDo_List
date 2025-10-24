from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('todo_list', views.todo_list, name='todo_list'),
    
    # URL da API (JSON)
    path('api/tarefas/', views.tarefa_list_create, name='tarefa-api'),
    path('api/tarefas/<int:id>/', views.tarefa_update_delete, name='tarefa-api-detail')

]
