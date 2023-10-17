# Importando a bibliotéca pandas para trabalhar com o csv.
import pandas as pd

# Lendo o arquivo csv e passando segundo parâmentro para padronizar com ';'. Usando a função 'head' para usar as 5 primeiras linhas no teste.
df = pd.read_csv("./data.csv", sep = ';').head()

# Escolhendo três colunas do arquivo.
print(df[['idade', 'acoes', 'valor']])

