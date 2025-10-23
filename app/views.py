from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import datetime
from . import db_redis
# Create your views here.

def app(request):
    return render(request, 'index.html')

def todo_list(request):
    return render(request, 'todo_list.html')

# Criação da API 
@api_view(['GET', 'POST']) # Agora a view aceita requests GET e POST
def tarefa_list_create(request):
    if request.method == 'GET':
        tarefas = db_redis.listar_tarefas()
        return Response(tarefas) # lista de tarefas como JSON
    
    elif request.method == 'POST':
        titulo = request.data.get('titulo') # como o DRF pega o JSON do front-end
        if not titulo:
            return Response({'erro': "O título é obrigatório"}, status=status.HTTP_400_BAD_REQUEST) 
        
        data_atual = datetime.date.today().isoformat()

        novo_id = db_redis.criar_tarefa(
            titulo = titulo,
            descricao = request.data.get('descricao', ''),
            data_criacao = data_atual,
            status = 'pendente'
        )
        
        nova_tarefa = db_redis.ler_tarefa(novo_id)
        nova_tarefa['id'] = novo_id

        return Response(nova_tarefa, status = status.HTTP_201_CREATED)