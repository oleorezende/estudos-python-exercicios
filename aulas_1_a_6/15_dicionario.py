# %%
dados_teo = {
    "sobrenome": "Calvo",
    "nome": "Téo",
    "filhos": True,
    "formacao": ["estatistica", "bigdata datascience"],
    "cargos": [
        {"nome": "ds jr.", "empresa": "tapps"},
        {"nome": "ds pl.", "empresa": "sas"},
        {"nome": "ds sr.", "empresa": "boticario"},
        {"nome": "ds espec.", "empresa": "via varejo"},
    ]
}

print(dados_teo)

# %%

print(dados_teo["formacao"][-1])
print(dados_teo["cargos"][-1]["empresa"])
# %%
dados_teo["estado civil"] = "casado"
# %%

print("chaves: ", dados_teo.keys())
print("Valores: ", dados_teo.values())
print ("Items: ", dados_teo.items())
# %%
 