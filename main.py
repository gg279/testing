import flet as ft

def main(page: ft.Page):
    page.title = "Simple Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Create a TextField to display the calculation
    display = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=300, readonly=True)

    # Variable to hold the current input and result
    current_input = ""

    # Function to handle button clicks
    def button_click(e):
        nonlocal current_input

        button_value = e.control.data

        if button_value == "C":
            current_input = ""
            display.value = "0"
        elif button_value == "=":
            try:
                result = str(eval(current_input))
                display.value = result
                current_input = result
            except:
                display.value = "Error"
                current_input = ""
        else:
            current_input += button_value
            display.value = current_input

        page.update()

    # Calculator buttons layout
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", "C", "=", "+"],
    ]

    # Create buttons and layout
    button_controls = []
    for row in buttons:
        button_row = []
        for button in row:
            button_row.append(ft.ElevatedButton(text=button, data=button, on_click=button_click, expand=True))
        button_controls.append(ft.Row(button_row, expand=True))

    # Add components to the page
    page.add(
        display,
        ft.Column(button_controls, expand=True)
    )

ft.app(target=main)
