import numpy as np
import sympy as sp
from grafico_interpolacao import grafico_mtpl


def interpolacao_Lagrange(matriz, tolerancia=None, saida_latex=False):
    r'''
    Funcao que recebe os valores de X e Y em forma de matriz.
    A partir destes valores, monta uma string polinomial,
    resolvendo-a com sympy.

    Entrada:
        matriz = valores de X e Y em forma de matriz numpy,
        recomenda-se que a matriz seja em formato string.
        saida_latex = retorna a equação Pn(X) no formato LaTeX.
        Exemplo simbolico de matriz:
            [['X0' 'X1' ... 'Xn']
             ['Y0' 'Y1' ... 'Yn']]
        Exemplo numerico de matriz:
            [['-1' '0' '1' '2']
             ['1' '1' '0' '-1']]
    ---
    Saida:
        funcao Pn(X)
        Exemplo, saida_latex = False:
            x**3/6 - x**2/2 - 2*x/3 + 1
        Exemplo, saida_latex = True:
            \frac{x^{3}}{6} - \frac{x^{2}}{2} - \frac{2 x}{3} + 1
    '''
    polinomio = ""
    fator = ""
    for Xi, Fi in zip(dados[0], dados[1]):
        for Xj in dados[0]:
            if Xj != Xi:
                fator += "*((x-({j}))/({i}-({j})))".format(i=Xi, j=Xj)
        polinomio += "+({f}){L}".format(f=Fi, L=fator)
        fator = ""
    x = sp.Symbol('x')
    polinomio = sp.simplify(sp.sympify(polinomio))
    polinomio = sp.nsimplify(polinomio, tolerance=tolerancia)
    if saida_latex:
        return sp.latex(polinomio)
    else:
        return polinomio


if __name__ == "__main__":

    dados = np.loadtxt("dados7.txt", dtype=str, delimiter=';')
    dados = dados.transpose()
    equacao = interpolacao_Lagrange(dados, tolerancia=0.001)
    print(equacao)
    grafico_mtpl(equacao, dados)
