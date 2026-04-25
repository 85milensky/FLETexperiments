import flet as ft
from flet import Page, Text, KeyboardEvent, Row

def main(page: Page) -> None:
    page.title = "Keyboard PRO"
    page.spacing = 30
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    #Create the text views
    key: Text = Text("Key", size = 30)
    shift: Text = Text("Shift", size = 30, color = "red")
    ctrl: Text = Text("Control", size = 30, color = "blue")
    alt: Text = Text("Alt", size = 30, color = "green")
    #space: Text = Text("Space", size = 30, color = "yellow") 

    #Handling KeyboardEvent
    def on_keyboard(e: KeyboardEvent) -> None:
        key.value = e.key
        shift.visible = e.shift
        ctrl.visible = e.ctrl
        alt.visible = e.alt

        print(e.data)
        page.update()

    #Link keyboard events to the page
    page.on_keyboard_event = on_keyboard

    #create a base page
    page.add(
        Text("Press any combination of keys ..."),
        Row(controls = [key, shift, ctrl, alt], alignment = ft.MainAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.run(main)
