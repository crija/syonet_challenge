import psycopg2

class BancoDeDados:
    def __init__(self):
        # Se conecta com o banco de dados.
        self.conexao = psycopg2.connect(
            database = 'postgres',
            user = 'postgres',
            password = 'postgres',
            host = 'localhost', 
            port = '5432'
        )

        # Seta configuração de auto realizar as queries.
        self.conexao.autocommit=True

    # Executa queries (comandos SQL) no Banco de Dados.
    def executar_query(self, query):
        cursor = self.conexao.cursor()
        cursor.execute(query)

        # Retorna o resultado da query.
        return cursor.fetchall()
