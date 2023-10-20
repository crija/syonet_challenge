# Importando a bibliotéca pandas para trabalhar com o csv.
import pandas as pd

# Importando os módulos da pasta analisadores.
from analisadores.analisador_idade import AnalisadorIdade
from analisadores.analisador_acoes import AnalisadorAcoes
from analisadores.analisador_valor import AnalisadorValor

from banco_de_dados import BancoDeDados

# Criando conexão com o Banco de Dados.
db = BancoDeDados()

db.executar_query('drop table analises_recompra')
# Criando tabela analises_recompra.
db.executar_query("""
CREATE TABLE IF NOT EXISTS analises_recompra(
    id SERIAL PRIMARY KEY,
    numero_linha INT,
    pontuacao INT,
    nome_arquivo VARCHAR,
    dados JSONB
);
""")

db.executar_query("""
CREATE UNIQUE INDEX IF NOT EXISTS idx_analises_recompra_arquivo_nome
ON analises_recompra(numero_linha, nome_arquivo);
""")

NOME_ARQUIVO = 'data.csv'
# Lendo o arquivo csv e passando segundo parâmentro para padronizar com ';'.
df = pd.read_csv(f"./{NOME_ARQUIVO}", sep = ';')

# Programa principal ao qual os três analisadores atuam.
for i, dados in df.iterrows(): # Estrutura de repetição, onde vai analisar cada linha do arquivo csv.
    ponto1 = AnalisadorIdade.analisar(dados)
    ponto2 = AnalisadorAcoes.analisar(dados)
    ponto3 = AnalisadorValor.analisar(dados)

    # Soma dos valores finais de cada coluna.
    pontuacao_total = ponto1 + ponto2 + ponto3
    numero_linha = i + 2

    # Passando dados para o Banco de Dados.
    db.executar_query(f"""
    INSERT INTO analises_recompra (
        numero_linha,
        pontuacao,
        nome_arquivo,
        dados
    ) VALUES (
        {numero_linha},
        {pontuacao_total},
        '{NOME_ARQUIVO}',
        '{dados.to_json()}'
    ) ON CONFLICT DO NOTHING
    """)