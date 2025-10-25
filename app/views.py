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
        descricao = request.data.get('descricao', '')
        if not titulo:
            return Response({'erro': "O título é obrigatório"}, status=status.HTTP_400_BAD_REQUEST) 
        
        data_atual = datetime.datetime.now().isoformat()

        novo_id = db_redis.criar_tarefa(
            titulo = titulo,
            descricao = descricao,
            data_criacao = data_atual,
            status = 'pendente'
        )
        
        nova_tarefa = db_redis.ler_tarefa(novo_id)
        nova_tarefa['id'] = novo_id

        return Response(nova_tarefa, status = status.HTTP_201_CREATED)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def tarefa_update_delete(request, id):
    if not db_redis.ler_tarefa(id):
        return Response({'erro':'Tarefa não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
    try:
        if request.method == 'GET':
            tarefa = db_redis.ler_tarefa(id)
            tarefa['id'] = id
            return Response(tarefa)
        elif request.method == 'PATCH': # Atualização parcial
            novo_status = request.data.get('status')

            if novo_status not in ['pendente', 'em andamento', 'concluída']:
                return Response({'erro':'Status inválido.'}, status=status.HTTP_400_BAD_REQUEST)
            
            db_redis.atulizar_tarefa(id, status = novo_status)

            tarefa_atualizada = db_redis.ler_tarefa(id)
            tarefa_atualizada['id'] = id
            return Response(tarefa_atualizada)
        elif request.method == 'DELETE':
            db_redis.excluir_tarefa(id)
            return Response(status=status.HTTP_204_NO_CONTENT) # Sucesso, mas sem corpo da resposta
    except Exception as e:
        return Response({'erro':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)