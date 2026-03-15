# %%
import requests
import json
from pathlib import Path
from tqdm import tqdm
import pandas as pd

ceps = ["18410295", "81200424"]

url = "https://viacep.com.br/ws/{cep}/json/"
dados = []

for cep in tqdm(ceps):
    resposta = requests.get(url.format(cep=cep))

    if resposta.status_code == 200:
        dados.append(resposta.json())

# %%
dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")
# %%
# pega a pasta do arquivo atual
pasta_script = Path(__file__).resolve().parent

arquivo = pasta_script / "ceps.json"

with open(arquivo, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)

print("Salvo em:", arquivo)
# %%
