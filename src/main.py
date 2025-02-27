import flet as ft
import json
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from authentication import authenticate_user  # Importa a autenticação

# Carregar variáveis de ambiente do ficheiro .env
load_dotenv()
SECRET = os.getenv("ENCRYPTION_KEY")

if not SECRET:
    raise ValueError("A chave de encriptação não foi encontrada")

encryptor = Fernet(SECRET)

class Task(ft.Column):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete
        self.display_task = ft.Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed
        )
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)

    def delete_clicked(self, e):
        self.task_delete(self)

class TodoApp(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.new_task = ft.TextField(
            hint_text="What needs to be done?", on_submit=self.add_clicked, expand=True
        )
        self.tasks = ft.Column()
        self.filter = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="all"), ft.Tab(text="active"), ft.Tab(text="completed")],
        )
        self.items_left = ft.Text("0 items left")
        self.controls = [
            ft.Row(
                [ft.Text(value="Tarefas", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                ],
            ),
            ft.Column(
                spacing=25,
                controls=[
                    self.filter,
                    self.tasks,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            self.items_left,
                            ft.OutlinedButton(text="Clear completed", on_click=self.clear_clicked),
                        ],
                    ),
                ],
            ),
        ]
        self.page.add(self)
        self.load_tasks()

    def add_clicked(self, e):
        if self.new_task.value:
            task = Task(self.new_task.value, self.task_status_change, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value = ""
            self.new_task.focus()
            self.save_tasks()
            self.update()

    def task_status_change(self, task):
        self.save_tasks()
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.save_tasks()
        self.update()

    def tabs_changed(self, e):
        self.update()

    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)
        self.save_tasks()

    def before_update(self):
        if hasattr(self, "filter") and self.filter is not None:
            status = self.filter.tabs[self.filter.selected_index].text
            count = 0
            for task in self.tasks.controls:
                task.visible = (
                    status == "all"
                    or (status == "active" and task.completed is False)
                    or (status == "completed" and task.completed)
                )
                if not task.completed:
                    count += 1
            self.items_left.value = f"{count} active item(s) left"

    def save_tasks(self):
        tasks_data = [
            {"name": task.display_task.label, "completed": task.completed}
            for task in self.tasks.controls
        ]
        encrypted_data = encryptor.encrypt(json.dumps(tasks_data).encode()).decode()
        self.page.client_storage.set("tasks", encrypted_data)

    def load_tasks(self):
        saved_tasks = self.page.client_storage.get("tasks")
        if saved_tasks:
            try:
                decrypted_data = encryptor.decrypt(saved_tasks.encode()).decode()
                tasks_data = json.loads(decrypted_data)
                for task_data in tasks_data:
                    task = Task(task_data["name"], self.task_status_change, self.task_delete)
                    task.completed = task_data["completed"]
                    task.display_task.value = task_data["completed"]
                    self.tasks.controls.append(task)
            except Exception as e:
                print("Erro ao desencriptar os dados:", e)
        self.update()

def main(page: ft.Page):
    page.title = "Gestor de Tarefas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    def start_app():
        page.clean()  # Limpa a tela após autenticação
        page.add(TodoApp(page))

    # 🚀 Autenticação antes de carregar o app
    authenticate_user(page, on_auth_success=start_app)

ft.app(main, port=1234, view=ft.WEB_BROWSER)
