class AnalisadorAcoes:
    def analisar(dados):
        if dados['acoes'] <= 2:
            return 10
        elif dados['acoes'] > 2 and dados['acoes'] <= 6:
            return 20
        elif dados['acoes'] > 6 and dados['acoes'] <= 9:
            return 30
        else:
            return 40