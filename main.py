from flet import app, Text, ElevatedButton

def main(page):
    def button_clicked(e):
        page.add(Text("Hello, World!"))
    page.add(ElevatedButton(text="Click Me", on_click=button_clicked))

app(target=main)
