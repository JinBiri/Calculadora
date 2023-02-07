import re, math
import tkinter as tk
from calc_create import *
from typing import List

# Instancia a class Calculator
class Calculator:
    def __init__(
        self,
        window: tk.Tk,
        label: tk.Label,
        display: tk.Entry,
        buttons: List[List[tk.Button]]
    ):
        self.window = window
        self.label = label
        self.display = display
        self.buttons = buttons


    def start(self):
        self._config_button()
        self._config_display()
        # Mantem a calculadora aberta, depois de iniciada
        self.window.mainloop()

    # Torna os botoes funcionais
    def _config_button(self):
        buttons = self.buttons
        # Seleciona uma linha
        for row_v in buttons:
            # Seleciona um botao dessa linha
            for button in row_v:
                # Guarda o texto desse botao
                button_text = button["text"]

                # Chama a função que limpa a tela
                if button_text == "C":
                    button.bind("<Button-1>", self.clear)
                    button.config(bg="#EA4335", fg="#fff")

                # Se o button_text conter algum operador ou numero, imprime esse valor no display
                if button_text in "0123456789.+-/*^()":
                    button.bind("<Button-1>", self.add_display)

                # Calcula o resultado
                if button_text == "=":
                    button.bind("<Button-1>", self.calculate)
                    button.config(bg="#4785f4", fg="#fff")
    
    # Torna a tecla enter funcional
    def _config_display(self):
        self.display.bind("<Return>", self.calculate)
        self.display.bind("<KP_Enter>", self.calculate)

    # Limpa a tela
    def clear(self, event=None):
        self.display.delete(0, "end")

    # Adiciona o valor do botao no display
    def add_display(self, event=None):
        self.display.insert("end", event.widget["text"])

    
    # Condiona a entrada, removendo caracteres indesejados
    def _fix_text(self, text):

        # Substitui tudo que não for 0123456789./*-+^ para nada
        text = re.sub(r"[^\d\.\/\*\-\+\^\(\)e]", r"", text, 0)

        # Substitui operadores repetidos para apenas um sinal
        text = re.sub(r"([\.\+\/\-\*\^])\1+", r"\1", text, 0)

        # Substitui () ou *() para nada
        text = re.sub(r"\*?\(\)", "", text)

        return text

    # Calcula o resultado final 
    def calculate(self, event=None):
        fixed_text = self._fix_text(self.display.get())
        equations = self._get_equations(fixed_text)
        
        # Tenta resolver as esquações
        try:
            # Se for apenas uma conta simples, resolve
            if len(equations) == 1:
                result = eval(self._fix_text(equations[0]))
            # Se for complexa, realiza cada parte separadamente
            else:
                result = eval(self._fix_text(equations[0]))
                for equation in equations[1:]:
                    result = math.pow(result, eval(self._fix_text(equation)))

            # Apaga o que estva no display e imprime o resultado da equação
            self.display.delete(0, "end")
            self.display.insert("end", result)
            self.label.config(text=f"{fixed_text} = {result}")

        # Erro de conta excessivamente grande
        except OverflowError:
            self.label.config(text="Não consigo resolver isso")
        # Qualquer outro erro
        except Exception:
            self.label.config(text="Operação invalida")
        
    # Separa a entrada em partes
    def _get_equations(self, text):
        return re.split("\^", text, 0)

# Cria a calculadora e a inicia
def main():
    window = make_window()
    display = make_display(window)
    label = make_label(window)
    buttons = make_buttons(window)
    calc = Calculator(window, label, display, buttons)
    calc.start()
    

if __name__ == "__main__":
    main()