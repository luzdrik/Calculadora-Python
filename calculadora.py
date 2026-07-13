##      Projeto 1 - Calculadora    (22/06/2026)     ##

import operations
import inputs

programa = True
print("\n==================================\n" \
"Bem-vindo(a) à calculadora Python!\n" \
"==================================")

menu = ("\nEscolha a operação desejada:\n" \
"1 - Adição\n" \
"2 - Subtração\n" \
"3 - Multiplicação\n" \
"4 - Divisão\n" \
"5 - Potenciação\n" \
"6 - Radiciação\n" \
"7 - Divisão inteira\n" \
"8 - Resto da Divisão\n" \
"0 - Sair")

while programa:
    print(menu)
    try:
        opcao = int(input("\n-> Opção: "))
    except ValueError:
        print("Digite um número válido.")
        continue
    
    if opcao == 0:
        print("\nAté a próxima! :)")
        programa = False

    elif opcao == 1:
        print("\n=== OPERAÇÃO: ADIÇÃO ===")
        num1, num2 = inputs.ler2()
        resultado = operations.soma(num1,num2)
        print("Resultado: ", resultado)

    elif opcao == 2:
        print("\n=== OPERAÇÃO: SUBTRAÇÃO ===")
        num1, num2 = inputs.ler2()
        resultado = operations.subtracao(num1,num2)
        print("Resultado: ", resultado)

    elif opcao == 3:
        print("\n=== OPERAÇÃO: MULTIPLICAÇÃO ===")
        num1, num2 = inputs.ler2()
        resultado = operations.multiplicacao(num1,num2)
        print("Resultado: ", resultado)

    elif opcao == 4:
        print("\n=== OPERAÇÃO: DIVISÃO ===")
        num1, num2 = inputs.ler2()
        resultado = operations.divisao(num1,num2)
        print("Resultado: ", resultado)

    elif opcao == 5:
        print("\n=== OPERAÇÃO: POTENCIAÇÃO ===")
        num1, num2 = inputs.ler2()
        resultado = operations.potenciacao(num1,num2)
        print("Resultado: ", resultado)

    elif opcao == 6:
        print("\n=== OPERAÇÃO: RADICIAÇÃO ===")
        num1 = input.ler1()

        resultado = operations.radiciacao(num1)
        print("Resultado: ", round(resultado, 2))

    elif opcao == 7:
        print("\n=== OPERAÇÃO: DIVISÃO INTEIRA ===")
        num1, num2 = inputs.ler2()
        resultado = operations.divisao_inteira(num1,num2)
        print("Resultado: ", resultado)

    elif opcao == 8:
        print("\n=== OPERAÇÃO: RESTO DA DIVISÃO ===")
        num1, num2 = inputs.ler2()
        resultado = operations.divisao_resto(num1,num2)
        print("Resultado: ", resultado)
