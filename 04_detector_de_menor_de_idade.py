# %%
# Faça um programa que receba o nome e a idade de uma pessoa. 

# Caso essa pessoa tenha menos de 18 anos, exiba o aviso:
#	“Fulano, você não pode dirigir nem beber”
#
# Para as pessoas entre 18 e 65 anos, exiba o aviso:
# 	“Fulano, bebida liberada! Só não vale dirigir!”
# 
# Para as pessoas com mais de 65 anos, exiba o aviso:
#	“Fulano, beba com muita moderação!”

try:

    idade = int(input("Me diga sua idade"))

    if idade < 18:
        print ("Você não pode beber")
    elif idade >= 65:
        print ("Até pode beber, mas com muita moderação")
    else:
        print ("Pode beber!")
        
except:
    print("Digite apenas números")

# %%

# %%
