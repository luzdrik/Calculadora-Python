##      Projeto 1 - Calculadora    (22/06/2026)     ##

import operations
import inputs

programa = True
print("\n==================================\n" \
"Bem-vindo(a) à calculadora Python!\n" \
"==================================")

MENU = """ 
Escolha a operação desejada:\n \
1 - Adição\n \
2 - Subtração\n \
3 - Multiplicação\n \
4 - Divisão\n \
5 - Potenciação\n \
6 - Radiciação\n \
7 - Divisão inteira\n \
8 - Resto da Divisão\n \
0 - Sair
"""

operacoes = {
    1: operations.soma,
    2: operations.subtracao,
    3: operations.multiplicacao,
    4: operations.divisao,
    5: operations.potenciacao,
    6: operations.radiciacao,
    7: operations.divisao_inteira,
    8: operations.divisao_resto
}

while programa:
    print(MENU)
    opcao = inputs.ler_inteiro("-> Opção: ")

    if opcao == 0:
        print("\nAté a próxima! :)")
        programa = False

    elif opcao == 1:
        print("\n=== OPERAÇÃO: ADIÇÃO ===")
        num1, num2 = inputs.ler2()
        resultado = operacoes[1](num1,num2)
        print("Resultado: ", resultado)

    elif opcao == 2:
        print("\n=== OPERAÇÃO: SUBTRAÇÃO ===")
        num1, num2 = inputs.ler2()
        resultado = operacoes[2](num1,num2)
        print("Resultado: ", resultado)

    elif opcao == 3:
        print("\n=== OPERAÇÃO: MULTIPLICAÇÃO ===")
        num1, num2 = inputs.ler2()
        resultado = operacoes[3](num1,num2)
        print("Resultado: ", resultado)

    elif opcao == 4:
        print("\n=== OPERAÇÃO: DIVISÃO ===")
        num1, num2 = inputs.ler2()
        resultado = operacoes[4](num1,num2)
        print("Resultado: ", resultado)

    elif opcao == 5:
        print("\n=== OPERAÇÃO: POTENCIAÇÃO ===")
        num1, num2 = inputs.ler2()
        resultado = operacoes[5](num1,num2)
        print("Resultado: ", resultado)

    elif opcao == 6:
        print("\n=== OPERAÇÃO: RADICIAÇÃO ===")
        num1 = inputs.ler1()
        resultado = operacoes[6](num1)
        print("Resultado: ", round(resultado, 2))

    elif opcao == 7:
        print("\n=== OPERAÇÃO: DIVISÃO INTEIRA ===")
        num1, num2 = inputs.ler2()
        resultado = operacoes[7](num1,num2)
        print("Resultado: ", resultado)

    elif opcao == 8:
        print("\n=== OPERAÇÃO: RESTO DA DIVISÃO ===")
        num1, num2 = inputs.ler2()
        resultado = operacoes[8](num1,num2)
        print("Resultado: ", resultado)
    else:
        print("Opção inválida.")
