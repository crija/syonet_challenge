# syonet_challenge
Challenge proposed by the company Syonet

### Objetivo:
 Criar um projeto em python para classificação de clientes com MAIS probabilidade de recompra de veículos.

#### Material Fornecido:
- [Arquivo CSV](data.csv)

#### Teste Manual:
Realizar testes manuais para garantir a qualidade das informações que serão armazenadas. Para isso usarei apenas três colunas e as 5 primeiras linhas.
- idade: Idade do carro;
- valor: Valor do carro;
- acoes: Quantidade de ações que o consumidor tomou para compra ou venda de carros.

#### Bibliotecas:
- Pandas: Leitura do arquivo csv.
- Psycopg2: Para o Python conseguir se comunicar com o Banco de Dados.

Atenção: O arquivo deve estar na mesma pasta do código.

#### Banco de Dados:
- Postgres: Para armazenar os dados dos clientes.

#### Organização Código:
- Criação do aquivo principal e pasta contendo os aquivos analisadores. Os analisadores foram criados com o intuito de analisar dados das colunas e adicionar pontos, onde serão somados e usados na probabilidade final.

#### Tempo de Pocessamento:
- Tempo de processamento fazendo uma inserção por linha do arquivo no banco de dados:
```sh
$ time python main.py
python main.py  44,16s user 4,49s system 31% cpu 2:33,69 total
```

#### Comandos Postgres:
Seleciona o número de linhas contidas no banco de dados.
```sql
$ select count(*) from analises_recompra;
```

Seleciona as colunas 'id', 'numero_linha', 'pontuacao' e nome_arquivo.
```sql
$ select id, numero_linha, pontuacao, nome_arquivo from analises_recompra;
```

Seleciona as colunas 'id', 'numero_linha', 'pontuacao' e 'nome_arquivo' que tenham a pontuação maior de 50.
```sql
$ select id, numero_linha, pontuacao, nome_arquivo from analises_recompra where pontuacao > 50;
```

Seleciona as colunas 'id', 'pontuacao' de forma ordenada, menor a maior pontuação.
```sql
$ select id, pontuacao, from analises_recompra order by pontuacao;
```

Seleciona a maior e menor pontuação.
```sql
$ select max(pontuacao), min(pontuacao) from analises_recompra;
```
