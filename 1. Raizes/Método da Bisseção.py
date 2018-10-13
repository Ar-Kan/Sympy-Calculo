# -*- coding: cp1252 -*-
import sympy as sp
from grafico_raiz import grafico_mtpl


def met_Bissecao(equacao, intervalo, precisao, decimais, nIterac):
    r'''
    equacao = equa��o
    amplitude = amplitude, intervalo inicial, lista de dois valores
    precis = precis�o dos c�lculos, amanho do intervalo [a;b],
             valor fracion�rio no intervalo {0;1}
    decis = quantos d�gitos ap�s a v�rgula, valor inteiro
    nIterac = n�mero m�ximo de itera��es
    '''
    x = sp.Symbol('x')
    Ya = equacao.subs({x: intervalo[0]})
    Yb = equacao.subs({x: intervalo[1]})
    if Ya * Yb > 0:
        return "sinal", 0

    Xa = sp.sympify(intervalo[0])
    Xb = sp.sympify(intervalo[1])
    iteracoes = 0
    while True:
        X_atual = ((Xa + Xb) / 2).evalf()
        Y_atual = equacao.subs({x: X_atual})

        if Y_atual == 0 or abs(Xa - Xb) <= precisao:
            if X_atual == 0:
                X_atual = 0
            break
        elif Y_atual != 0:
            if Y_atual * Ya < 0:
                Xb = X_atual
            elif Y_atual * Yb < 0:
                Xa = X_atual
            iteracoes += 1

        if iteracoes >= nIterac:
            return None, iteracoes
    cont = 0
    teste = int(abs(X_atual))
    while teste >= 1:
        teste /= 10
        cont += 1
    valor = sp.N(X_atual, decimais + cont)
    return valor, iteracoes


if __name__ == "__main__":
    print('''Determina��o de ra�z de uma equa��o atrav�s do m�todo da secante \n''')

    x = sp.Symbol('x')
    expressao = sp.sympify("x**3-9*x+3")
    ampl = [2, 3]
    prec = 0.0006
    decis = 3
    max_iter = 100

    raiz, iterac = met_Bissecao(expressao, ampl, prec, decis, max_iter)
    if raiz == "sinal":
        print("A fun��o {} n�o possui sinais opostos nos pontos {} e {}.".format(expressao, ampl[0], ampl[1]))
    elif raiz is None:
        print("O m�todo falhou em encontrar uma raiz, ap�s {} itera��es.".format(iterac))
    else:
        print("A ra�z obtida, ap�s {n} itera��es, �: {s}.".format(n=iterac, s=raiz))
        grafico_mtpl(expressao, raiz)
