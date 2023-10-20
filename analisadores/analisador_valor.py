class AnalisadorValor:
    def analisar(dados):
        if dados['valor'] <= 30000.0:
            return 40
        elif dados['valor'] > 30000.0 and dados['valor'] <= 60000.0:
            return 30
        elif dados['valor'] > 60000.0 and dados['valor'] <= 90000.0:
            return 20
        else:
            return 10