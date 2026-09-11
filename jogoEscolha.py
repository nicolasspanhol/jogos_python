import random 

print("Jogo da Escolha!")

for i in range (3):
    usuario = int(input("Escolha um número de 1 a 10: "))

    if usuario > 10 or usuario == 0:
        print("Escolha errada, tente novamente!")
        continue
    
numero_pc = random.randint(1, 10)

if usuario == numero_pc:
    print("Você acertou!")
else: 
    print("Você errou, tente novamente!")
    

print("O PC escolheu: ", numero_pc)



