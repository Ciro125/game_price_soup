import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

link = "https://gg.deals/deals/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
requisicao = requests.get(link, headers = headers)

print(requisicao)
# print(requisicao.text)

site = BeautifulSoup(requisicao.text, "html.parser")
# print(site.prettify())

# print(site.title)

titulo_jogo = site.find_all("a", class_="game-info-title title")
precos_velho = site.find_all("span", class_="price-label price-old")
precos_novo = site.find_all("span", class_="price-inner game-price-new")
print(titulo_jogo)
print("\n")
print(precos_velho)
print("\n")
print(precos_novo)
print("\n")
# print(precos_novo.get_text())

print(len(titulo_jogo), len(precos_velho), len(precos_novo))


# Criar listas com os textos dos elementos
titulos = [titulo.text for titulo in titulo_jogo]
precos_velho_texto = [preco_velho.text for preco_velho in precos_velho]
precos_novo_texto = [preco_novo.text for preco_novo in precos_novo]

# Certificar-se de que as listas têm o mesmo comprimento
min_length = min(len(titulos), len(precos_velho_texto), len(precos_novo_texto))

# Criar dicionário com os dados
data = {
    'titulo_jogo': titulos[:min_length],
    'precos_velho': precos_velho_texto[:min_length],
    'precos_novo': precos_novo_texto[:min_length]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Substituir valores vazios por NaN
df.replace('', np.nan, inplace=True)

# Converter os preços para formato numérico (removendo o "R$" e convertendo para float)
df['precos_velho'] = pd.to_numeric(df['precos_velho'].replace('[\D]', '', regex=True), errors='coerce')

# Tratar os casos especiais para "Free" no preço novo
df['precos_novo'] = df['precos_novo'].replace('Free', '0')
df['precos_novo'] = pd.to_numeric(df['precos_novo'].replace('[\D]', '', regex=True), errors='coerce')

# Exibir DataFrame
print(df)