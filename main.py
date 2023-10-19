# Importando a bibliotéca pandas para trabalhar com o csv.
import pandas as pd

# Importando os módulos da pasta analisadores. 
from analisadores.analisador_idade import AnalisadorIdade
from analisadores.analisador_acoes import AnalisadorAcoes
from analisadores.analisador_valor import AnalisadorValor

from banco_de_dados import BancoDeDados

# Criando conexão com o Banco de Dados.
db = BancoDeDados()
# Criando tabela analises_recompra.
db.executar_query(""" 
CREATE TABLE IF NOT EXISTS analises_recompra(
    numero_linha INT,
    pontuacao INT
);
""")

# Lendo o arquivo csv e passando segundo parâmentro para padronizar com ';'.
df = pd.read_csv("./data.csv", sep = ';').head() # Usando a função 'head' para usar as 5 primeiras linhas do arquivo no teste.

# Programa principal ao qual os três analisadores atuam.
for i, dados in df.iterrows(): # Estrutura de repetição, onde vai analisar cada linha do arquivo csv, gerando uma pontuação.
    ponto1 = AnalisadorIdade.analisar(dados)
    ponto2 = AnalisadorAcoes.analisar(dados)
    ponto3 = AnalisadorValor.analisar(dados)

    pontuacao_total = ponto1 + ponto2 + ponto3
    numero_linha = i + 2

    db.executar_query(f"INSERT INTO analises_recompra (numero_linha, pontuacao) VALUES ({numero_linha}, {pontuacao_total})")

    



    



        


    