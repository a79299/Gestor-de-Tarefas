# Gestor de Tarefas - Flet

## Descrição
Este é um aplicativo de Gestão de Tarefas desenvolvido com Flet, uma biblioteca para criar aplicações web e desktop em Python. O projeto inclui autenticação via GitHub OAuth 2.0, armazenamento local de tarefas e uma interface responsiva.

## Funcionalidades
- **Adicionação de Tarefas**: Permite adicionar novas tarefas.
- **Edição e Remoção**: Tarefas podem ser editadas ou excluídas.
- **Filtragem**: Filtra as tarefas por "Todas", "Ativas" ou "Concluídas".
- **Armazenamento Persistente**: Os dados são criptografados e armazenados localmente.
- **Autenticação via GitHub**: Login seguro via GitHub OAuth 2.0.
- **Animação de Carregamento**: Tela de carregamento antes da autenticação.
- **favicon**: Emoji Personalizado para a app.
- **Deploy no Replit**: Hospedagem na web através do Replit.

## Tecnologias Utilizadas
- [Flet] - Interface gráfica.
- [Cryptography] - Encriptação de dados.
- [Dotenv] - Gestor das variáveis de ambiente.
- [GitHub OAuth] - Autenticação segura.

## Autenticação via GitHub OAuth
O sistema de login utiliza OAuth via GitHub, garantindo segurança e facilidade de acesso. O Utilizador deve autenticar-se para acessar a aplicação.

### Como funciona:
1. Ao iniciar, o sistema exibe um botão "Login com GitHub".
2. O utilizador é redirecionado para a página de autenticação do GitHub.
3. Após a autenticação, o sistema exibe o nome e a foto do utilizador.
4. O utilizador pode fazer logout a qualquer momento.

## Instalação e Configuração

### Clonar o repositório
```bash
git clone https://github.com/a79299/Gestor-de-Tarefas.git
cd Gestor-de-Tarefas
```

### Criar e ativar um ambiente virtual (opcional)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### Instalar dependências
```bash
pip install flet
```

### Configurar variáveis de ambiente
No ficheiro `.env` mude as credenciais para as suas:
```
GITHUB_CLIENT_ID=SEU_CLIENT_ID
GITHUB_CLIENT_SECRET=SEU_CLIENT_SECRET
```

### Executar o projeto
```bash
flet run main.py --web --port 1234
```
Acesse no navegador: `http://127.0.0.1:1234`

**Dica**: Caso encontre algum problema, verifique se todas as dependências estão instaladas e se as variáveis de ambiente estão configuradas corretamente.