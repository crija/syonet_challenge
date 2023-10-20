class AnalisadorIdade:
    def analisar(dados):
        if dados['idade'] < 25:
            return 10
        elif dados['idade'] > 25 and dados['idade'] <= 40:
            return 20
        elif dados['idade'] > 40 and dados['idade'] <= 65:
            return 30
        else:
            return 40
