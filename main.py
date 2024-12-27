import flet as ft

def main(page: ft.Page):
    page.title = "Simple To-Do App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # List to store tasks
    tasks = ft.Column()

    # Function to add a task
    def add_task(e):
        task_text = task_input.value
        if task_text.strip():
            tasks.controls.append(
                ft.Row(
                    [
                        ft.Text(task_text),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            on_click=lambda _: delete_task(task_text),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            )
            task_input.value = ""
            page.update()

    # Function to delete a task
    def delete_task(task_text):
        for control in tasks.controls:
            if control.controls[0].value == task_text:
                tasks.controls.remove(control)
                break
        page.update()

    # Input field and button for adding tasks
    task_input = ft.TextField(hint_text="Enter a task", expand=True)
    add_button = ft.ElevatedButton("Add Task", on_click=add_task)

    # Add controls to the page
    page.add(
        ft.Column(
            [
                ft.Row([task_input, add_button]),
                tasks,
            ]
        )
    )

# Run the app
ft.app(target=main)
