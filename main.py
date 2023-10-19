# Importando a bibliotéca pandas para trabalhar com o csv.
import pandas as pd

# Importando os módulos da pasta analisadores. 
from analisadores.analisador_idade import AnalisadorIdade
from analisadores.analisador_acoes import AnalisadorAcoes
from analisadores.analisador_valor import AnalisadorValor

from banco_de_dados import BancoDeDados

# Lendo o arquivo csv e passando segundo parâmentro para padronizar com ';'.
df = pd.read_csv("./data.csv", sep = ';').head() # Usando a função 'head' para usar as 5 primeiras linhas do arquivo no teste.

# Mostrar as colunas e valores.
print(df)

# Programa principal ao qual os três analisadores atuam.
for i, dados in df.iterrows(): # Estrutura de repetição, onde vai analisar cada linha do arquivo csv, gerando uma pontuação.
    ponto1 = AnalisadorIdade.analisar(dados)
    ponto2 = AnalisadorAcoes.analisar(dados)
    ponto3 = AnalisadorValor.analisar(dados)
    print(f'Total de pontos da linha {i}: {ponto1 + ponto2 + ponto3}') # Somando os pontos de cada linha.

    
db = BancoDeDados()
resultado = db.executar_query("select 'Hello World'")
print(resultado)



    



        


    