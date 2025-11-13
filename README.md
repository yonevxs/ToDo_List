# To-Do List com Django, Redis e TailwindCSS

Um aplicativo de lista de tarefas (To-Do List) desenvolvido com Django. Este projeto utiliza Django Rest Framework para a API, Redis (com `django-redis`) para gerenciamento de dados ou cache, e Tailwind CSS para a estilização do front-end.

## ✨ Features

* Funcionalidade CRUD (Criar, Ler, Atualizar, Excluir) para tarefas.
* Interface de usuário moderna estilizada com Tailwind CSS.
* API RESTful construída com Django Rest Framework para gerenciar as tarefas.
* Integração com Redis para alta performance no acesso aos dados.

## 🛠️ Tecnologias Utilizadas

### ⚙️ **Backend & Banco de Dados**
<div>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40" alt="Python"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="40" height="40" alt="Django"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" width="40" height="40" alt="Redis"/>
</div>

**Principais tecnologias e dependências:**
- **Python** – Linguagem principal da aplicação.  
- **Django** – Framework web para desenvolvimento robusto e escalável.  
- **Django Rest Framework (DRF)** – Criação e gerenciamento de APIs RESTful.  
- **Redis** – Armazenamento em cache e gerenciamento de sessões.  
- **django-redis** – Integração do Redis com o Django para cache e otimização.  

---

### 🎨 **Frontend**
<div>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="40" height="40" alt="HTML5"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-original.svg" width="40" height="40" alt="TailwindCSS"/>
</div>

**Principais tecnologias:**
- **HTML5** – Estruturação semântica das páginas.  
- **Tailwind CSS** – Framework CSS utilitário para estilização responsiva e moderna.  

---

### 📦 **Outras dependências (do `requirements.txt`)**
- **asgiref** – Suporte para aplicações assíncronas no Django.  
- **sqlparse** – Formatação e análise de consultas SQL.  
- **tzdata** – Gerenciamento de fusos horários para aplicações Django.  


## 🚀 Pré-requisitos

Antes de começar, você precisará ter as seguintes ferramentas instaladas em sua máquina:
* [Python 3.x](https://www.python.org/downloads/)
* [Node.js e npm](https://nodejs.org/en/) (para o Tailwind CSS)
* [Redis](https://redis.io/topics/quickstart) (um servidor Redis deve estar em execução)
* Pip (gerenciador de pacotes do Python)

## ⚙️ Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento local:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    cd SEU-REPOSITORIO
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # (Opcional, mas recomendado)
    python -m venv venv
    
    # No Windows
    .\venv\Scripts\activate
    
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências do Python:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Navegue até a pasta do projeto** (onde está o `package.json`):
    ```bash
    cd ToDo_List
    ```

5.  **Instale as dependências do Node.js (Tailwind):**
    ```bash
    npm install
    ```

6.  **Configure o Redis:**
    * Certifique-se de que seu servidor Redis esteja rodando (normalmente na porta `6379`).
    * Verifique o arquivo `settings.py` do Django para garantir que as configurações de conexão com o Redis (`CACHES` ou similar) estão corretas.

## ▶️ Rodando a Aplicação

Você precisará de **dois terminais** abertos, ambos na pasta `ToDo_List`.

1.  **Terminal 1: Rodar o Tailwind CSS (modo "watch"):**
    * Este comando irá monitorar seus arquivos HTML e de template, recompilando o CSS automaticamente sempre que houver uma alteração.
    ```bash
    npm run watch:css
    ```

2.  **Terminal 2: Rodar o servidor Django:**
    * Este comando iniciará o servidor de desenvolvimento do Django.
    ```bash
    py manage.py runserver
    ```

Agora, você pode acessar o aplicativo em [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no seu navegador.

---

## 🧪 Testando o CRUD via CLI

O projeto inclui um script `main.py` que permite testar as operações CRUD diretamente pelo terminal (provavelmente interagindo com a API ou os models).

1.  Certifique-se de que o servidor Django (`py manage.py runserver`) esteja em execução.
2.  Em um **novo terminal**, na pasta `ToDo_List`, execute:
    ```bash
    python main.py
    ```
---

## 👥 Contribuidores

Este projeto foi desenvolvido pela seguinte equipe:

* **Gabriel Nobre**
* **Gustavo Lemos**
* **Kalebe Menezes**
* **Lucas Neves**
* **Nicolas da Silva**
