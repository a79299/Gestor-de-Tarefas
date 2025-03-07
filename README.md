# Gestor de Tarefas com Flet e Autenticação GitHub

## Descrição
Este é um aplicativo web de gestão de tarefas (To-Do List) desenvolvido com [Flet]. O objetivo é permitir que os Utilizadores possam gerir as suas tarefas diárias de forma simples e intuitiva. Além disso, o projeto inclui autenticação via GitHub OAuth e armazenamento seguro das tarefas utilizando criptografia com a biblioteca `cryptography`.

## Funcionalidades
- **Autenticação com GitHub OAuth**: Login seguro utilizando GitHub.
- **Criação de tarefas**: Permite adicionar novas tarefas.
- **Edição de tarefas**: Possibilidade de renomear as tarefas.
- **Marcação de tarefas como concluídas**: As tarefas podem ser marcadas como "feitas".
- **Filtragem de tarefas**:
  - Todas as tarefas
  - Somente ativas
  - Somente concluídas
- **Exclusão de tarefas**: Remova tarefas individualmente ou em lote.
- **Armazenamento criptografado**: Os dados das tarefas são armazenados de forma segura e localmente.
- **Interface intuitiva**: Desenvolvida utilizando Flet para facilitar o uso.

## Tecnologias Utilizadas
- **Linguagem**: Python 3.8+
- **Framework**: [Flet]
- **Autenticação**: GitHub OAuth
- **Segurança**: [Cryptography] para encriptação dos dados
- **Gestão de variáveis de ambiente**: [Python-dotenv]

## Requisitos
Antes de rodar o projeto, certifique-se de ter instalado:
- Python 3.8+
- Pip

Também será necessário configurar um aplicativo OAuth no GitHub e obter as credenciais:
- `GITHUB_CLIENT_ID`
- `GITHUB_CLIENT_SECRET`
- `REDIRECT_URL`

## Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/a79299/Gestor-de-Tarefas.git
   ```
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Execução
Para iniciar o aplicativo, execute:
```sh
python main.py
```
O aplicativo abrirá automaticamente no navegador.

## Como Funciona o Projeto
### 1. **Autenticação**
A aplicação requer que o utilizador faça login com sua conta do GitHub. Isso é feito através do GitHub OAuth, que redireciona o utilizador para a página de login do GitHub e retorna um token de autenticação para a aplicação.

### 2. **Gestão de Tarefas**
Depois que o utilizador está autenticado, ele pode adicionar, editar, excluir e filtrar suas tarefas. Cada tarefa é salva localmente utilizando `client_storage` do Flet, e os dados são criptografados antes do armazenamento.

### 3. **Armazenamento Seguro**
As tarefas são armazenadas em formato JSON e encriptadas com `cryptography.fernet` antes de serem salvas localmente. Isso garante que os dados não possam ser acessados diretamente sem a chave de encriptação.

### 4. **Interface Gráfica**
A interface do utilizador é baseada em componentes visuais do Flet, utilizando `ft.Column`, `ft.Row`, `ft.Checkbox`, `ft.TextField` e `ft.Button`. As interações do utilizador, como adicionar ou editar tarefas, são manipuladas com eventos `on_click` e `on_change`.
