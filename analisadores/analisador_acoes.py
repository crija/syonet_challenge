class AnalisadorAcoes:
    def analisar(dados):
        if dados['acoes'] < 2:
            return 5
        elif dados['acoes'] > 2 and dados['acoes'] <=  4:
            return 10
        else:
            return 12