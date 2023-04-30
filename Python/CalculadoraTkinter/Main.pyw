import tkinter as tk
import calcular_vetor
import converter_str_vetor
class Calculadora:
    def __init__(self, janela):
        self.janela = janela
        janela.title("Calculadora")

        # Cria o visor
        self.visor = tk.Entry(janela, width=25, font=("Arial", 16))
        self.visor.grid(row=0, column=0, columnspan=4)

        botoes = [
            "7","8","9","*",
            "4","5","6","/",
            "1","2","3","-",
            "0",'.',"+","="
        ]
        
        # Cria os botões
        p = 0
        k = 1
        for i in botoes:
            if i != "=":
                botao = tk.Button(janela, text=i, width=5, height=2, font=("Arial", 12),
                                  command=lambda i=i: self.atualizar_visor(i))
                botao.grid(row=k, column=p)
            else:
                botao = tk.Button(janela, text=i, width=5, height=2, font=("Arial", 12),
                                  command=lambda : self.calcular())
                botao.grid(row=k, column=p)
            p += 1
            if p == 4:
                k += 1
                p = 0


        # Cria o botão "="
        """botao = tk.Button(janela, text="=", width=5, height=2, font=("Arial", 12),
                          command=lambda: self.calcular())
        botao.grid(row=4, column=2)"""


    def atualizar_visor(self, valor):
        self.visor.insert(tk.END, valor)

    def calcular(self):
        vetor = converter_str_vetor.conversor(self.visor.get())
        resultado = calcular_vetor.calcular(vetor)
        self.visor.delete(0, tk.END)
        self.visor.insert(0, resultado)

    
janela = tk.Tk()
calculadora = Calculadora(janela)
janela.mainloop()
