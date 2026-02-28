# Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

comprar = """Oii, o que você quer comprar?
(1) laranja
(2) cerveja
(3) miojo
(4) carvão
(5) picanha
"""

opcao = input(comprar)

if opcao == "1":
    print ("vc quer laranja né, toma ai")
elif opcao == "2":
    print ("você quer cerveja ne, bebado veio")
elif opcao == "3":
    print ("você quer miojo")
elif opcao == "4":
    print ("você quer carvao")
elif opcao == "5":
    print ("você quer picanha")
else:
    print ("essa eu n tenho")