from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app(request):
    return render(request, 'index.html')
def todo_list(request):
    return render(request, 'todo_list.html')