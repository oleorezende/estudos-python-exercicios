# %%
# LISTA → usa colchetes [] e pode ser modificada

dados_teo = [32, 1, "Casado", "dev golang"]

# podemos adicionar novos valores
dados_teo.append("3241.43")

# podemos alterar valores existentes
dados_teo[0] = 28

print(dados_teo)


# %%
# TUPLA → usa parênteses () e NÃO pode ser modificada (imutável)

# tupla_teo = 32, 1, "Casado", "dev golang"  # também é válido
tupla_teo = (32, 1, "Casado", "dev golang")

# mostra o tipo
print(type(tupla_teo))

# mostra o conteúdo
print(tupla_teo)


# %%
# isto gera erro, porque tuplas não podem ser alteradas
# tupla_teo[0] = 28