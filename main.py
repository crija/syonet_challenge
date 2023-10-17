import pandas as pd

df = pd.read_csv("./data.csv", sep = ';')
print(df[['idade', 'acoes', 'valor']])
