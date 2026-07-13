def ler1():
    num1 = int(input("* Informe um número: "))
    return num1

def ler2():
    num1 = int(input("* Informe o primeiro número: "))
    num2 = int(input("* Informe o segundo número: "))
    return num1, num2

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")