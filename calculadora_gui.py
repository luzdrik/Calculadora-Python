import tkinter as tk

janela = tk.Tk()

janela.title("Calculadora")
janela.geometry("350x500")

visor = tk.Entry(
    janela,
    font=("Arial", 20),
    justify="right",
    width=20
)
visor.grid(
    row=0,
    column=0,
    columnspan=4
)

# Criação dos botões
for i in range(9):

    linha = i // 3
    coluna = i % 3

    botao = tk.Button(
        janela,
        text=str(i),
        width=5,
        height=2
    )
    botao.grid(row=linha + 1, column=coluna)

janela.mainloop()