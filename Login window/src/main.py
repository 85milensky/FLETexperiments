import flet as ft
from flet import ControlEvent, TextField, Checkbox, Text, Row, Column, ControlEvent, Button

def main(page: ft.Page) -> None:
   
    #setup window
    page.title = "Signup"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.STRETCH
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window.height = 350
    page.window.width = 350
    page.window.resizable = False

    #setup fields
    text_username: TextField = TextField(label = "Username", text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label = "Password", text_align=ft.TextAlign.LEFT, width=200)
    checkbox_signup: Checkbox = Checkbox(label = "I agree!", value = False)
    button_submit: Button = Button( content = "Submit", width = 200, disabled=True) #(text = "Submit", width = 200, disabled = True)

    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value == True]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        
        page.update()

    def submit(e: ControlEvent) -> None:
        print('Username:', text_username.value)
        print('Password:', text_password.value)

        page.clean()

        page.add(
            Column(
                controls=[
                    Text(value="Signup successful!", size=20, weight=ft.FontWeight.BOLD)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
            )
        )

    #render the signup page
    page.add(
        Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                Column([
                        text_username,
                        text_password,
                        checkbox_signup,
                        button_submit
                        ]
                    )
                ]
            )
        )

    #link functions to events
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

if __name__ == "__main__":
    ft.run(main)
