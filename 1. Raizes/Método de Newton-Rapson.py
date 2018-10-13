# -*- coding: cp1252 -*-
import sympy as sp
from grafico_raiz import grafico_mtpl


def newton_Raphson(equacao, valor, precisao, decimais, nIterac):
    r'''
    equacao = equação
    valor = valor do x inicial
    precisao = precisão dos cálculos, para quando a diferença entre
        um resultado e o resultado anterior é menor ou igual à
        essa precisão, valor fracionário no intervalo {0;1}
    decimais = quantos dígitos após a vírgula, valor inteiro
    nIterac = número máximo de iterações
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
    print('''Determinação de raíz de uma equação através do método Newton-Raphson \n''')

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
        print("O método falhou em encontrar uma raiz, após {} iterações.".format(iterac))
    else:
        print("y = x - ({e})/({d})".format(e=expressao, d=deriv))
        print("A raíz obtida, após {n} iterações, é: {s}.".format(n=iterac, s=raiz))
        grafico_mtpl(expressao, raiz)
