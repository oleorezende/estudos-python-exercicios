# Faça um programa que receba 4 notas de um aluno. 
# Retorne a média dessas notas, a menor e a maior nota:

#Média: x
# Menor: y
# Maior: z
# %%

notastotais = []

while True:
    notas = input("Me diga suas notas")

    if notas == "":
        break
    notas = int(notas)
    notastotais.append(notas)

media = sum(notastotais) / len(notastotais)
maior = max(notastotais)
menor = min(notastotais)

print ("Sua media de nota foi: ", media, 
       ", e sua maior nota foi: ", maior, 
       ", e sua menor nota foi: ", menor)

    
    
# %%
