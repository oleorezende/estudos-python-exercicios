#Faça um programa que vende uma garrafa de água:
#Se o cliente escolher água mineral natural, será cobrado R$1,50
#Se o cliente escolher água mineral com gás, será cobrado R$2,50

texto = """
Escolha a sua Água
(1) Água mineral
(2) Água sabor gás
"""

opcao = input(texto)
if opcao == "1":
    print ("Sua conta deu R$ 1,50")
elif opcao == "2":
    print ("Sua conta deu R$ 2,50")
else:
    print ("entre com a porra da opção correta")