from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('todo_list', views.todo_list, name='todo_list')
]
