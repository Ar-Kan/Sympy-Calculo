# -*- coding: cp1252 -*-
import sympy as sp
from grafico_raiz import grafico_mtpl


def newton_Raphson(equacao, valor, precisao, decimais, nIterac):
    r'''
    equacao = equa��o
    valor = valor do x inicial
    precisao = precis�o dos c�lculos, para quando a diferen�a entre
        um resultado e o resultado anterior � menor ou igual �
        essa precis�o, valor fracion�rio no intervalo {0;1}
    decimais = quantos d�gitos ap�s a v�rgula, valor inteiro
    nIterac = n�mero m�ximo de itera��es
    '''
    x = sp.Symbol('x')
    derivada = sp.diff(equacao, x)
    iteracoes = 0
    while True:
        valor_atual = (valor - equacao.subs({x: valor}) /
                       derivada.subs({x: valor})).evalf()

        err_fun = abs(equacao.subs({x: valor_atual}))

        if valor_atual == valor or err_fun <= precisao:
            if valor == 0:
                valor = 0
            break
        else:
            valor = valor_atual
            iteracoes += 1
        if iteracoes >= nIterac:
            return None, iteracoes, 0
    cont = 0
    teste = int(abs(valor))
    while teste >= 1:
        teste /= 10
        cont += 1
    valor = sp.N(valor_atual, decimais + cont)
    return valor, iteracoes, derivada


if __name__ == "__main__":
    print('''Determina��o de ra�z de uma equa��o atrav�s do m�todo Newton-Raphson \n''')

    x = sp.Symbol('x')
    expressao = sp.sympify("x**3-9*x+3")
    ponto_ini = 4
    prec = 0.006
    decis = 3
    max_iter = 100

    raiz, iterac, deriv = newton_Raphson(expressao,
                                         ponto_ini,
                                         prec,
                                         decis,
                                         max_iter)
    if raiz is None:
        print("O m�todo falhou em encontrar uma raiz, ap�s {} itera��es.".format(iterac))
    else:
        print("y = x - ({e})/({d})".format(e=expressao, d=deriv))
        print("A ra�z obtida, ap�s {n} itera��es, �: {s}.".format(n=iterac, s=raiz))
        grafico_mtpl(expressao, raiz)
