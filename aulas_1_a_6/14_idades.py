# %%
idades = []

while True:
    idade = input("entre com idade: ")
    if idade == "": 
        break
    
    idades.append(int(idade))

print (idades)

media = sum(idades)/ len(idades)
minimo = min(idades)
maximo = max(idades)
qntda = len (idades)

print ("MEDIA: ", int(media))
print ("MINIMO: ", minimo)
print ("MAXIMO: ", maximo)
print ("QUANTIDADE: ", qntda)
# %%
