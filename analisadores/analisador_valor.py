class AnalisadorValor:
    def analisar(dados):
        if dados['valor'] <= 50000.0:
            return 15
        elif dados['valor'] > 50000.0 and dados['valor'] < 80000.0:
            return 8
        else:
            return 5