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
    
class AnalisadorIdade:
    def analisar(dados):
        if dados['idade'] >= 30:
            return 1
        else:
            return -1
        
class AnalisadorAcoes:
    def analisar(dados):
        if dados['acoes'] >= 2:
            return 1
        else:
            return -1
        
class AnalisadorValor:
    def analisar(dados):
        if dados['valor'] < 100000.0:
            return 1
        else:
            return -1
        
for i, dados in df.iterrows():
    ponto1 = AnalisadorIdade.analisar(dados)
    ponto2 = AnalisadorAcoes.analisar(dados)
    ponto3 = AnalisadorValor.analisar(dados)
    print(f'Total de pontos da linha {i}: {ponto1 + ponto2 + ponto3}')
    







    '''if j['acoes'] >= 2:
        cont =+ 1
        #print(f"idade: {j['idade']} = {cont} | acoes: {j['acoes']} = recebe: {cont}")
    elif j['acoes'] < 2:
        cont =- 1
        print(f"idade: {j['idade']} = {cont} | acoes: {j['acoes']} = recebe: {cont}")'''



    



        


    