# Task Manager App 💻

## Índice

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Uso](#uso)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Descrição

O **Task Manager App** é uma aplicação de gerenciamento de tarefas que permite aos usuários criar, visualizar, atualizar e excluir tarefas. É uma ferramenta útil para organizar suas atividades diárias e aumentar a produtividade.

## Funcionalidades

- Adicionar novas tarefas com descrição e data de vencimento.
- Visualizar todas as tarefas em uma lista.
- Editar as informações de uma tarefa existente.
- Excluir tarefas que já foram concluídas ou não são mais necessárias.
- Marcar tarefas como concluídas.

## Instalação

Para executar o Task Manager App localmente, siga estas etapas:

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/task-manager-app.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd task-manager-app
    ```

3. Crie um ambiente virtual (recomendado) e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/macOS
    venv\Scripts\activate  # Para Windows
    ```

4. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

5. Configure o banco de dados (Postgres):

    - Crie um banco de dados chamado `task_manager`.
    - Atualize o arquivo `config.py` com as credenciais do seu banco de dados.

6. Execute as migrações do banco de dados:

    ```bash
    alembic upgrade head
    ```

7. Inicie o servidor FastAPI:

    ```bash
    uvicorn app.main:app --reload
    ```

8. Acesse a aplicação em [http://localhost:8000](http://localhost:8000).

## Uso

Você pode interagir com a API usando o Postman ou diretamente pelo navegador em [http://localhost:8000/docs](http://localhost:8000/docs), onde encontrará a documentação interativa gerada pelo Swagger UI.

## Tecnologias Utilizadas

- **Backend**: FastAPI
- **Banco de Dados**: PostgreSQL
- **Gerenciamento de Dependências**: Pipenv / virtualenv
- **Documentação da API**: Swagger UI (integrado com FastAPI)

## Contribuição

Contribuições são bem-vindas! Para contribuir com este projeto:

1. Faça um fork do repositório.
2. Crie uma nova branch: `git checkout -b feature/nova-feature`.
3. Faça suas alterações e commit: `git commit -m 'Adiciona nova feature'`.
4. Envie para o branch original: `git push origin feature/nova-feature`.
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações ou perguntas, entre em contato com:

- Nome: João Vitor
- Email: joaovitorbarbosa513@gmail.com
- GitHub: [Dev-barbosajv](https://github.com/Dev-barbosajv)
