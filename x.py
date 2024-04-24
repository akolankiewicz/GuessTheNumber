import random

numero_secreto = random.randint(1, 100)
tentativas = 0
print("Adivinhe o número secreto entre 1 e 100.")
while True:
    tentativa = int(input("Tentativa: "))
    tentativas += 1
    if tentativa < numero_secreto:
        print("Tente um número maior.")
    elif tentativa > numero_secreto:
        print("Tente um número menor.")
    else:
        print(f"Parabéns! Você adivinhou corretamente em {tentativas} tentativas.")
        break
