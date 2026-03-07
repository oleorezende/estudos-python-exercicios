# Construa um programa que realiza o sorteio de um número entre 1 e 15
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

# %%

def get_input():
    while True:
        try:
            numero_usuario = int(input("Diga teu numero"))
        
        except ValueError:
            print("Valor invalido! O valor deve ser entre 1 e 15!")
            continue

        if not 1 <= numero_usuario <= 15:
            print("Valor invalido! O valor deve ser entre 1 e 15!")
            continue

        return numero_usuario


print ("Acerte o numero de 1 a 15 com 3 tentativas!")

import random

numero_sorteio = random.randint(1,15)

for i in range(3):
        
        print(f"Tentativas restantes: {3-i}")
        
        numero_usuario = get_input()

        if numero_sorteio == numero_usuario:
            print("Parabens você acertou o numero")
            break

        elif numero_usuario > numero_sorteio:
            print("Errou! Diga um numero menor!")

        else:
            print("Errou! Diga um numero maior!")
    
else:
    print(f"Você perdeu! O número sorteado era {numero_sorteio}")

# %%
