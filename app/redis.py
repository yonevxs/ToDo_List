import redis 

r = redis.Redis(
    host='redis-12616.crce196.sa-east-1-2.ec2.redns.redis-cloud.com',
    port=12616,
    decode_responses=True,
    username="default",
    password="cU01voxTnuo2BsTfhACs4ro1Hw0HYkuh",
)

def criar_tarefa(id,titulo, descricao,data_criacao,status):

    chave = f"tarefa:{id}"
    
    dados = {
            "titulo" : titulo,
            "descricao": descricao,
            "data_criacao" : data_criacao,
            "status": status
    }
    r.hset(chave,mapping=dados)


def ler_tarefa(id):
    chave = f"tarefa:{id}"    
    return r.hgetall(chave)    


def atulizar_tarefa(id,titulo= None, descricao = None ,data_criacao = None,status = None):

    chave = f"tarefa:{id}"

    dados = {}

    if titulo is not None:
        dados['titulo'] = titulo
    if descricao is not None:
        descricao['descricao'] = descricao
    if data_criacao is not None:
        data_criacao['data_criacao'] =  data_criacao
    if status is not None:
        status['status'] =  status

    if dados:
        r.hset(chave,mapping=dados)
        return True
    else:
        return False


def excluir_tarefa(id):
 
    chave = f"tarefa:{id}"
    

    deletar = r.hdel(chave)

    if deletar == 1:
        return "Tarefa Deletada"
    else:
        return "Tarefa não Deletada"
     