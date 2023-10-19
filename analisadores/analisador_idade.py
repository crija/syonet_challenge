class AnalisadorIdade:
    def analisar(dados):
        if dados['idade'] < 30:
            return 5
        elif dados['idade'] > 30 and dados['idade'] <= 50:
            return 15
        else:
            return 25
        