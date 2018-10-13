# -*- coding: cp1252 -*-
import sympy as sp
from grafico_raiz import grafico_mtpl


def met_Secante(equacao, intervalo, precisao, decimais, nIterac):
    r'''
    equacao = equa��o
    intervalo = amplitude, intervalo inicial, lista de dois valores
    precisao = precis�o dos c�lculos, para quando a diferen�a entre
        um resultado e o resultado anterior � menor ou igual �
        essa precis�o, valor fracion�rio no intervalo {0;1}
    decimais = quantos d�gitos ap�s a v�rgula, valor inteiro
    nIterac = n�mero m�ximo de itera��es
    '''
    x = sp.Symbol('x')
    iteracoes = 0
    while True:
        funcXi = equacao.subs({x: intervalo[0]})
        funcXj = equacao.subs({x: intervalo[1]})
        valor_atual = ((intervalo[0] * funcXj - intervalo[1] * funcXi) /
                       (funcXj - funcXi)).evalf()
        intervalo[0] = intervalo[1]
        intervalo[1] = valor_atual

        err_funcao = abs(equacao.subs({x: intervalo[1]}).evalf())
        err_intervalo = abs(intervalo[1] - intervalo[0])

        if err_funcao <= precisao or err_intervalo <= precisao:
            if intervalo[1] == 0:
                intervalo[1] = 0
            break
        else:
            iteracoes += 1
        if iteracoes >= nIterac:
            return None, iteracoes
    cont = 0
    teste = int(abs(intervalo[1]))
    while teste >= 1:
        teste /= 10
        cont += 1
    valor = sp.N(intervalo[1], decimais + cont)
    return valor, iteracoes


if __name__ == "__main__":
    print('''Determina��o de ra�z de uma equa��o atrav�s do m�todo da secante \n''')

    x = sp.Symbol('x')
    expressao = sp.sympify("x**3-9*x+3")
    ampl = [2, 3]
    prec = 0.006
    decis = 3
    max_iter = 100

    raiz, iterac = met_Secante(expressao, ampl, prec, decis, max_iter)
    if raiz is not None:
        print("A ra�z obtida, ap�s {n} itera��es, �: {s}.".format(n=iterac, s=raiz))
        grafico_mtpl(expressao, raiz)
    else:
        print("O m�todo falhou em encontrar uma raiz, ap�s {} itera��es.".format(iterac))
