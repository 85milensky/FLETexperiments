import flet as ft
from flet import Row, Text, Button, MainAxisAlignment, ControlEvent, Page

class incrementCounter(Row):

    def __init__(self, text: str, start_number: int = 0) -> None:
        
        #setup state
        super().__init__()
        #self.text = text
        self.counter= start_number
        self.text_number: Text = Text(value = str(start_number), size = 40)

        #configure row properties
        self.alignment = MainAxisAlignment.SPACE_BETWEEN
        self.width = 300

        #define children
        self.controls = [
            Button(text, on_click = self.increment),
            self.text_number
        ]

    def increment(self, e: ControlEvent) -> None:
        self.counter += 1
        self.text_number.value = str(self.counter)
        self.update()

def main(page: Page) -> None:
    page.title = "Reusable App"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    page.add(incrementCounter("People", 10))
    page.add(incrementCounter("Animals", 15))

if __name__ == "__main__":
    ft.run(main)
