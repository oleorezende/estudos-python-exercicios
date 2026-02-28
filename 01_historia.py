# Faça um programa que dê bom dia;
# Faça um programa que de bom dia, pergunta o nome da pessoa e responde que é um prazer conhecer ela, citando o nome da pessoa.
# Crie uma história simples. Adicione essa história em um programa. A cada parágrafo, a história deve aguardar o usuário apertar “enter” para dar continuidade.
# Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.
# Faça um programa que exiba o dobro de um número inserido pelo usuário.

# %%
nome = input("Qual o seu nome?")
print ("Bom dia,", nome,"tudo bem?")
print ("é um prazer te conhecer!")
input("vou te contar uma historia")
input("era 3 porquinhos")
input("ai eles tavam andando")
input("caiu e morreu")

# %%
numero = input("Me fala um numero ai, que vou falar a raiz quadrada!")
numero = int(numero)
print ("a raiz quadrade de", numero, "é", numero ** 0.5)
# %%
dobro = input("agora vou falar o dobro do numero ai q tu falar ")
dobro = int(dobro)
print ("o dobro de", dobro, "é", dobro * 2)