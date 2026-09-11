import random 

print("Jogo da Escolha!")

numero_pc = random.randint(1, 10)

for i in range (3):
    usuario = int(input("Escolha um número de 1 a 10: "))

    if usuario < 1 or usuario > 10:
        print("Escolha errada, tente novamente com um número de 1 a 10!")
        continue
    
    if usuario == numero_pc:
        print("Você acertou!")
        break
    else: 
        print("Você errou, tente novamente!")
    
print("O PC escolheu: ", numero_pc)



