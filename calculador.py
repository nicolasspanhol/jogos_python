opcao = 0
while opcao != 5:

    print("CALCULADORA")
    print("1 - Somar")
    print("2- Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        resultado = numero1 + numero2

        print("O resultado é: ", resultado)
        

    elif opcao == 2:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        resultado = numero1 - numero2
        
        print("O resultado é: ", resultado)
        

    elif opcao == 3:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        resultado = numero1 * numero2
        
        print("O resultado é: ", resultado)
        

    elif opcao == 4:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        resultado = numero1 / numero2
        
        print("O resultado é: ", resultado)
        

    else:
        print("Você escolheu sair, até mais!")
        break