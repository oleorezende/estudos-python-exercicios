# Escreva um programa que receba uma lista de números
# do usuário e conte quantas vezes um número
# específico aparece na lista.
# Solicite ao usuário um número e exiba a contagem.
#  %%
lista = [1,6,5,9,9,59,65,66,6,6,1,2,3]

numero = input("Entre com o numero: ")
numero = int(numero)

contador = 0
for i in lista:
    if i == numero:
        contador += 1

print("o numero", numero, "nessa lista se repete", contador, "vezes")
# %%
# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

texto = "banana"
contador = 0
for i in texto:
    if i == "a":
        contador += 1

print("Quantidade de 'a':", contador)


print(texto)
# %%
