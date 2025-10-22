# main.py
import db_redis
import datetime

def mostrar_menu():
    print("\n--- To-Do List com Redis ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Todas as Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Excluir Tarefa")
    print("5. Sair")
    return input("Escolha uma opção: ")

def adicionar_tarefa_interativo():
    print("\n--- Adicionar Nova Tarefa ---")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data_hoje = datetime.date.today().isoformat()
    
    # Usando a função que gera o ID automaticamente
    novo_id = db_redis.criar_tarefa(
        titulo=titulo,
        descricao=descricao,
        data_criacao=data_hoje,
        status="pendente"
    )
    print(f"Tarefa criada com sucesso! ID: {novo_id}")

def listar_tarefas_interativo():
    print("\n--- Suas Tarefas ---")
    tarefas = db_redis.listar_tarefas() # Usando a função de listar todas
    
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for tarefa in tarefas:
        # Pega o ID (a função listar_tarefas já deve incluir)
        id_tarefa = tarefa.get('id', 'ID não encontrado') 
        print(f"  ID: {id_tarefa}")
        print(f"  Título: {tarefa.get('titulo')}")
        print(f"  Descrição: {tarefa.get('descricao')}")
        print(f"  Status: {tarefa.get('status')}")
        print("  --------------------")

def atualizar_tarefa_interativo():
    print("\n--- Atualizar Status da Tarefa ---")
    try:
        id_tarefa = int(input("Digite o ID da tarefa para concluir: "))
        
        # Verifica se a tarefa existe antes de atualizar
        if not db_redis.ler_tarefa(id_tarefa):
             print("Erro: Tarefa com este ID não existe.")
             return

        db_redis.atulizar_tarefa(id_tarefa, status="concluída")
        print(f"Tarefa {id_tarefa} marcada como concluída!")
    except ValueError:
        print("Erro: ID inválido. Deve ser um número.")

def excluir_tarefa_interativo():
    print("\n--- Excluir Tarefa ---")
    try:
        id_tarefa = int(input("Digite o ID da tarefa a excluir: "))
        resultado = db_redis.excluir_tarefa(id_tarefa)
        print(resultado)
    except ValueError:
        print("Erro: ID inválido. Deve ser um número.")

# --- Loop Principal da Aplicação ---
def main():
    # Antes de começar, verifique se a função listar_tarefas existe
    if not hasattr(db_redis, 'listar_tarefas'):
        print("Erro: A função 'listar_tarefas' não foi encontrada em db_redis.py.")
        print("Por favor, adicione a função para listar todas as tarefas (como na resposta anterior).")
        return
        
    while True:
        escolha = mostrar_menu()
        
        if escolha == '1':
            adicionar_tarefa_interativo()
        elif escolha == '2':
            listar_tarefas_interativo()
        elif escolha == '3':
            atualizar_tarefa_interativo()
        elif escolha == '4':
            excluir_tarefa_interativo()
        elif escolha == '5':
            print("Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

# Garante que o main() só rode quando executamos "python main.py"
if __name__ == "__main__":
    main()