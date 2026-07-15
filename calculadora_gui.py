import tkinter as tk
import operations as op

# Criação da janela
janela = tk.Tk()

janela.title("Calculadora")
janela.geometry("350x500")

# Visor da calculadora
visor = tk.Entry(
    janela,
    font=("Arial", 20),
    justify="right",
    width=20
)

# Inicia com o 0 setado
visor.insert(0, "0")

visor.grid(
    row=0,
    column=0,
    columnspan=4
)

# Criando um vetor na ordem dos botões do teclado de uma calculadora
botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

operacoes = {
    "+": op.soma,
    "-": op.subtracao,
    "*": op.multiplicacao,
    "/": op.divisao
}

# Criando variáveis globais
num1 = None
num2 = None
operador = None

# Criando funções
def limpar():
    visor.delete(0, tk.END)
    visor.insert(tk.END, "0")

def clicar_numero(valor):
    if visor.get() == "0":
        visor.delete(0, tk.END)
        
    visor.insert(tk.END, valor)

def calcular():
    
    pass

# Dicionário de ações da interface
acoes = {
    "C": limpar,
    "=": calcular
}

def clique(valor):
    if valor in acoes:
        acoes[valor]()

    elif valor in operacoes:
        num1 = int(visor.get())
        operador = valor

        visor.delete(0, tk.END)

    else:
        clicar_numero(valor)


"""acoes = {
    "C": limpar,
    #"=": calcular,
    #"+": adicionar,
    #"-": subtrair
}"""

# Widgets
## Criação dos botões
for i, texto in enumerate(botoes):

    linha = i // 4
    coluna = i % 4

    botao = tk.Button(
        janela,
        text=texto,
        width=8,
        height=2,
        command=lambda valor=texto: clique(valor)
    )
    botao.grid(
        row=linha + 1,
        column=coluna,
        padx=5,
        pady=5)

# Janela entra no estado de loop e espera interação
janela.mainloop()