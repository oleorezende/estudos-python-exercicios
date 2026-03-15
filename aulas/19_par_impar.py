# %%
def par_impar(numero:int):
    if numero % 2 == 0:
        print ("é par")
    else:
        print("é impar")

numero = input("Entre com um numero")
numero = int(numero)

par_impar(numero)