# %%
tempo= int(input ("Olá, me fala um tempo em segundos que irei te falar em horas e minutos!"))
horas = tempo// 3600
resto = tempo % 3600
minutos = resto // 60
segundos = resto % 60


print (f"{horas}:{minutos}:{segundos}")
# %%
