import flet as ft

def main(page: ft.Page):
    page.title = "Notepad App"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    #page.scroll = True - it seems that scroll is rendering the page unusable
    
    def save_text(e):
        with open("save.txt", "w") as f:
            f.write(textfield.value)

    def read_text():
        try:
            with open("save.txt", "r") as f:
                return f.read()
        except FileNotFoundError:
            return ""

    # Create the textfield directly
    textfield = ft.TextField(
        value=read_text(),
        multiline=True,
        autofocus=True,
        border=ft.InputBorder.OUTLINE,
        min_lines=20,
        expand=True, # This tells it to take up available space
        on_change=save_text,
        cursor_color="yellow",
        hint_text="Start typing here...",
    )

    # Wrap it in a Container to ensure it occupies physical space on the screen
    editor_container = ft.Container(
        content=textfield,
        expand=True,
    )

    page.add(editor_container)

if __name__ == "__main__":
    ft.run(main)