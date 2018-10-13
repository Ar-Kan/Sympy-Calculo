# -*- coding: cp1252 -*-
import sympy as sp
from grafico_raiz import grafico_mtpl


def met_Secante(equacao, intervalo, precisao, decimais, nIterac):
    r'''
    equacao = equação
    intervalo = amplitude, intervalo inicial, lista de dois valores
    precisao = precisão dos cálculos, para quando a diferença entre
        um resultado e o resultado anterior é menor ou igual à
        essa precisão, valor fracionário no intervalo {0;1}
    decimais = quantos dígitos após a vírgula, valor inteiro
    nIterac = número máximo de iterações
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
    print('''Determinação de raíz de uma equação através do método da secante \n''')

    x = sp.Symbol('x')
    expressao = sp.sympify("x**3-9*x+3")
    ampl = [2, 3]
    prec = 0.006
    decis = 3
    max_iter = 100

    raiz, iterac = met_Secante(expressao, ampl, prec, decis, max_iter)
    if raiz is not None:
        print("A raíz obtida, após {n} iterações, é: {s}.".format(n=iterac, s=raiz))
        grafico_mtpl(expressao, raiz)
    else:
        print("O método falhou em encontrar uma raiz, após {} iterações.".format(iterac))
