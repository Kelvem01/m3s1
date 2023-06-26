def decoretor_imprimir(funcao):

    def mensagem(*args, **kwargs):
       # função interna para imprimir o parametros originais 
        capital = args[0]
        taxa = args [1]
        tempo = args [2]
        print(f'CAPITAL: {capital}, TAXA:{taxa}, TEMPO:{tempo}')

        resultado = funcao(*args, **kwargs) # esta linha não esta funcionando ja refiz o codigp
        return resultado
    return mensagem

@decoretor_imprimir
def juros_simples(capital, taxa , tempo):
    return capital *(taxa/100)*tempo
