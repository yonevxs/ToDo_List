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
            dados_para_atualizar = {}
            
            # 1. VALIDAÇÃO E ATUALIZAÇÃO DO STATUS
            novo_status = request.data.get('status')
            if novo_status is not None:
                if novo_status not in ['pendente', 'em andamento', 'concluída']:
                    return Response({'erro':'Status inválido.'}, status=status.HTTP_400_BAD_REQUEST)
                dados_para_atualizar['status'] = novo_status
            
            # 2. ATUALIZAÇÃO DA DESCRIÇÃO (Se o campo estiver presente na requisição)
            nova_descricao = request.data.get('descricao')
            if nova_descricao is not None:
                dados_para_atualizar['descricao'] = nova_descricao
            
            # 3. ATUALIZAÇÃO DO TÍTULO (Se o campo estiver presente na requisição)
            novo_titulo = request.data.get('titulo')
            if novo_titulo is not None:
                dados_para_atualizar['titulo'] = novo_titulo
            
            # Checa se pelo menos um campo válido foi enviado
            if not dados_para_atualizar:
                return Response({'erro':'Nenhum campo válido para atualizar.'}, status=status.HTTP_400_BAD_REQUEST)
                
            # Chama a função de atualização, passando os dados coletados
            db_redis.atulizar_tarefa(id, **dados_para_atualizar)

            tarefa_atualizada = db_redis.ler_tarefa(id)
            tarefa_atualizada['id'] = id
            return Response(tarefa_atualizada)
        
        elif request.method == 'DELETE':
            db_redis.excluir_tarefa(id)
            return Response(status=status.HTTP_204_NO_CONTENT)
            
    except Exception as e:
        return Response({'erro':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)