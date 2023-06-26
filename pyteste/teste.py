import pytest # importando pyteste

def multplicacao(x,y):
    return x*y

def teste_multplicacao():
    m = multplicacao (10,3)
    try:
        assert m == 31
    except:
        raise AssertionError('Erro na multiplicação')
    print(m)


teste_multplicacao() 