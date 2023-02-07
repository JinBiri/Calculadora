import tkinter as tk
from typing import List

# Cria a janela da calculadora
def make_window() -> tk.Tk:
    window = tk.Tk()
    window.title("Calculator")
    window.config(padx=10, pady=10, background="#fff")
    window.resizable(False, False)

    return window

# Cria o texto que fica sob o display
def make_label(window) -> tk.Label:
    label = tk.Label(
        window, text="",
        anchor="e", justify="right", background="#fff"
    )
    label.grid(row=0, column=0, columnspan=5, sticky="news")

    return label

# Cria o display, que mostrará as equações
def make_display(window) -> tk.Entry:
    display = tk.Entry(window)
    display.config(
        font=("Helvetica", 40, "bold"),
        justify="right", bd=1, relief="flat",
        highlightthickness=1, highlightcolor="#ccc"
    )
    display.bind("<Control-a>", display_control_a)
    display.grid(row=1, column=0, columnspan=5, sticky="news", padx=(0, 10))

    return display

# Habilita o ctrl+a para selecionar o texto em display
def display_control_a(event):
    event.widget.select_range(0, "end")
    event.widget.icursor("end")
    return "break"

# Cria os botões com seus respectivos operadores
def make_buttons(window) -> List[List[tk.Button]]:
    buttons_texts: List[List[str]] = [
        ["7", "8", "9", "+", "C"],
        ["4", "5", "6", "-", "/"],
        ["1", "2", "3", "*", "^"],
        ["0", ".", "(", ")", "="]
    ]

    buttons: List[List[tk.Button]] = []
    # Para cada linha de botões
    for row, row_v in enumerate(buttons_texts, start=2):
        button_row = []
        # Para cada botão na linha
        for col_i, col_v in enumerate(row_v):
            btn = tk.Button(window, text=col_v)
            # Configura o botão
            btn.config(
                font=("Helvetica", 15, "normal"),
                pady=40, width=1, background="#f1f2f3", bd=0,
                cursor="hand2", highlightthickness=0, 
                highlightcolor="#ccc", activebackground="#ccc",
                highlightbackground="#ccc"
            )
            button_row.append(btn)
            btn.grid(row=row, column=col_i, sticky="news", padx=5, pady=5)

        buttons.append(button_row)

    return buttons

