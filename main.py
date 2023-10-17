# Importando a bibliotéca pandas para trabalhar com o csv.
import pandas as pd

# Lendo o arquivo csv e passando segundo parâmentro para padronizar com ';'. Usando a função 'head' para usar as 5 primeiras linhas no teste.
df = pd.read_csv("./data.csv", sep = ';').head()

# Escolhendo três colunas do arquivo.
df = df[['idade', 'acoes', 'valor']]

print(df)

#print(df.loc[df['idade'] == 31])

'''for linha in df.items():
    print(linha)'''
    
cont = 0
for i, j in df.iterrows():
    if j['idade'] >= 30:
        cont =+ 1
        print(f"{j['idade']} = {cont}")
    elif j['idade'] < 30:
        cont =- 1
        print(f"{j['idade']} = {cont}")
        print('---------')



        


    