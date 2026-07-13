##      Projeto 1 - Calculadora    (22/06/2026)     ##

import operations
import inputs

programa = True

BOAS_VINDAS = """
==================================
Bem-vindo(a) à calculadora Python!
==================================
"""

MENU = """ 
Escolha a operação desejada:
 1 - Adição
 2 - Subtração
 3 - Multiplicação
 4 - Divisão
 5 - Potenciação
 6 - Radiciação
 7 - Divisão inteira 
 8 - Resto da Divisão
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

nomes_operacoes = {
    1: "ADIÇÃO",
    2: "SUBTRAÇÃO",
    3: "MULTIPLICAÇÃO",
    4: "DIVISÃO",
    5: "POTENCIAÇÃO",
    6: "RADICIAÇÃO",
    7: "DIVISÃO INTEIRA",
    8: "RESTO DA DIVISÃO"
}

print(BOAS_VINDAS)
while programa:
    print(MENU)
    opcao = inputs.ler_inteiro("-> Opção: ")

    if opcao == 0:
        print("\nAté a próxima! :)")
        programa = False

    elif opcao in operacoes:
        
        print(f"\n=== OPERAÇÃO: {nomes_operacoes[opcao]} ===")

        if opcao == 6:
            num1 = inputs.ler1()
            resultado = operacoes[opcao](num1)

        else:
            num1, num2 = inputs.ler2()
            resultado = operacoes[opcao](num1,num2)
        
        print("Resultado: ", resultado)

    else:
        print("Opção inválida.")