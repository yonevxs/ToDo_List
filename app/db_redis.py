import redis 

r = redis.Redis(
    host='redis-12616.crce196.sa-east-1-2.ec2.redns.redis-cloud.com',
    port=12616,
    decode_responses=True,
    username="default",
    password="cU01voxTnuo2BsTfhACs4ro1Hw0HYkuh",
)

def criar_tarefa(titulo, descricao,data_criacao,status):

    id = r.incr("proximo_id_tarefa")
    chave = f"tarefa:{id}"
    
    dados = {
            "titulo" : titulo,
            "descricao": descricao,
            "data_criacao" : data_criacao,
            "status": status
    }
    r.hset(chave,mapping=dados)

    return id


def ler_tarefa(id):
    chave = f"tarefa:{id}"    
    return r.hgetall(chave)    


def atulizar_tarefa(id,titulo= None, descricao = None ,data_criacao = None,status = None):

    chave = f"tarefa:{id}"
    dados = {}

    if titulo is not None:
        dados['titulo'] = titulo
    if descricao is not None:
        dados['descricao'] = descricao
    if data_criacao is not None:
        dados['data_criacao'] =  data_criacao
    if status is not None:
        dados['status'] =  status

    if dados:
        r.hset(chave,mapping=dados)
        return True
    else:
        return False


def excluir_tarefa(id):
 
    chave = f"tarefa:{id}"

    deletar = r.delete(chave)

    if deletar == 1:
        return "Tarefa Deletada"
    else:
        return "Tarefa não Deletada"

def listar_tarefas():
    tarefas = []
    # Busca todas as chaves que começam com "tarefa:"
    chaves_tarefas = r.keys("tarefa:*")
    
    for chave in chaves_tarefas:
        # Pega o ID da chave (ex: "tarefa:1" -> "1")
        id_tarefa = chave.split(":")[-1]
        
        # Busca os dados do hash
        dados_tarefa = r.hgetall(chave)
        
        # Adiciona o ID aos dados
        dados_tarefa['id'] = id_tarefa
        
        tarefas.append(dados_tarefa)
        
    return tarefas
     