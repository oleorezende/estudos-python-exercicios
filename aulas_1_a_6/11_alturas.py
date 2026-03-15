# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas.

soma = 0  # valor final
qtde_entradas = 4  # o contador de entradas

while qtde_entradas > 0:
    altura = input("Entre com a altura: ")
    altura = float(altura) #é usado float pq se fosse usado INT ele ia somar os numeros inteiros
    qtde_entradas -= 1

print ("Soma das altura:", soma)