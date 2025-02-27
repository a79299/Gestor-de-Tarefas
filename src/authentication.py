import os
import flet as ft
from flet.auth.providers import GitHubOAuthProvider
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Credenciais do GitHub
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

# Verificar se as credenciais foram fornecidas corretamente
if not GITHUB_CLIENT_ID or not GITHUB_CLIENT_SECRET:
    raise ValueError("As credenciais do GitHub OAuth não foram encontradas no ambiente.")

# Configurar provedor OAuth do GitHub
provider = GitHubOAuthProvider(
    client_id=GITHUB_CLIENT_ID,
    client_secret=GITHUB_CLIENT_SECRET, 
    redirect_url="http://localhost:1234/oauth_callback",
)

def authenticate_user(page: ft.Page, on_auth_success):

    def login_click(e):
        page.login(provider)

    def logout_click(e):
        page.auth = None
        page.session.clear()
        page.clean()
        show_login()

    def on_login(e):
        if e.error:
            page.clean()
            page.add(ft.Text("Erro ao autenticar!", color="red"))
        else:
            page.clean()
            user = page.auth.user
            page.add(
                ft.Row(
                    [
                        ft.Text(f"Bem-vindo, {user['name']}!", size=20),
                        ft.Image(src=user.get("picture", "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"), width=50, height=50),
                        ft.ElevatedButton("Logout", on_click=logout_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
            on_auth_success()  # Chama a função que inicializa o app

    def show_login():
        page.add(ft.ElevatedButton("Login com GitHub", on_click=login_click))

    page.on_login = on_login
    show_login()