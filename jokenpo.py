# 1 atividade: adicionar 3 chances para jogar
import random

print("Jogo Jokenpo!")

opcoes = ["Pedra", "Papel", "Tesoura", "Martelo"]

for i in range(3):
    jogador = str(input("Escolha entre Pedra, Papel, Tesoura ou Martelo: ").capitalize())

    if jogador not in opcoes:
        print("Escolha errada tente novamente.")
        continue

    pc = random.choice(opcoes)

    print("O computador escolheu:", pc)

    if jogador == pc:
        print("Empate!")
    elif jogador == "Pedra":
        if pc == "Tesoura":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Papel":
        if pc == "Pedra":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Tesoura":
        if pc == "Papel":
            print("Você venceu!")
        else:
            print("O seu adversário venceu!")
    elif jogador == "Martelo":
        if pc == "Papel" or pc == "Tesoura":
            print("Você venceu!")
    else:
        print("O seu adversario venceu!")
