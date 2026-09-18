ariana = 0
sabrina = 0
taylor = 0

opcao = 0

while opcao != 4:

    print("=== VOTAÇÃO ===")
    print("1 - ARIANA GRANDE")
    print("2 - SABRINA CARPENTER")
    print("3 - TAYLOR SWIFT")
    print("4 - ENCERRAR VOTAÇÃO")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Voto registrado para Ariana Grande!")
        ariana += 1

    elif opcao == 2: 
        print("Voto registrado para Sabrina Carpenter!")
        sabrina += 1

    elif opcao == 3:
        print("Voto registrado para Taylor Swift!")
        taylor += 1

    elif opcao == 4:
        print("Votação Encerrada!")
        print("=== RESULTADO ===")
        print("Ariana Grande teve: ", ariana, "votos!")
        print("Sabrina Carpenter teve: ", sabrina, "votos!")
        print("Taylor Swift teve: ", taylor, "votos!")
        break

    else:
        print("Opção Inválida!")