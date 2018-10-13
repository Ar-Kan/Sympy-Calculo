import numpy as np
import sympy as sp
from sympy.abc import *
from grafico_mmq import grafico_mtpl


def coeficiente_A(matriz, grau):
    valores_A = (np.empty([grau + 1, grau + 1]) * np.nan)
    valores_A = (valores_A.reshape((grau + 1, grau + 1))).astype(str)
    somatorio = 0
    for Gi in range(grau + 1):
        for Gj in range(grau + 1):
            for Fk in range(len(matriz[0])):
                somatorio += sp.simplify(sp.sympify((sp.sympify(matriz[0][Fk])**Gi) *
                                                    (sp.sympify(matriz[0][Fk])**Gj)))
            valores_A[Gi][Gj] = str(somatorio)
            somatorio = 0
    return valores_A


def coeficiente_B(matriz, grau):
    valores_B = (np.empty([grau + 1, 1]) * np.nan)
    valores_B = (valores_B.reshape((grau + 1, 1))).astype(str)
    somatorio = 0
    for Gi in range(grau + 1):
        for Fk in range(len(matriz[0])):
            somatorio += sp.simplify(sp.sympify(sp.sympify(matriz[1][Fk]) *
                                                (sp.sympify(matriz[0][Fk])**Gi)))
        valores_B[Gi][0] = str(somatorio)
        somatorio = 0
    return valores_B


def coeficiente_Incog(grau):
    incognitas = np.array([a, b, c, d, e, f, g, h, i, j, k, l,
                           m, n, o, p, q, r, s, t, u, v, w, x, y, z]).reshape(26, 1)
    coeficientes = (np.empty([grau + 1, 1]) * np.nan).reshape((grau + 1, 1)).astype(object)
    for coef in range(grau + 1):
        coeficientes[coef][0] = incognitas[coef][0]
    return coeficientes


def sist_Equacoes(matriz, grau):
    matA = coeficiente_A(matriz, grau)
    matB = (coeficiente_B(matriz, grau)).transpose()
    matCoef = (coeficiente_Incog(grau)).transpose()
    sistema = (np.empty([grau + 1, 1]) * np.nan).reshape((grau + 1, 1)).astype(object)
    equacao = ''
    for linhaA in range(len(matA)):
        for colunaA in range(len(matA[0])):
            equacao += str(matA[linhaA][colunaA]) + '*' + str(matCoef[0][colunaA]) + '+'
            if colunaA == (len(matA[0]) - 1):
                equacao += '(-' + str(matB[0][linhaA]) + ')'
        sistema[linhaA][0] = sp.simplify(sp.sympify(equacao))
        equacao = ''
    return sistema, matCoef


def polinomio(matriz, grau, valores_coeficientes=False,
              em_decimais=False, tolerancia=None):
    equacoes, coefis = sist_Equacoes(matriz, grau)
    list_coef = []
    list_equa = []
    for item in range(len(coefis[0])):
        list_coef.append(coefis[0][item])
    for item in range(len(equacoes)):
        list_equa.append(equacoes[item][0])
    coef_value = sp.solve(list_equa, (list_coef))
    polinomio = ''
    for indice in range(len(list_equa)):
        polinomio += '+(' + str(coef_value[list_coef[indice]]) + ')*x**(' + str(indice) + ')'
    if not em_decimais:
        polinomio = sp.nsimplify(sp.sympify(polinomio), tolerance=tolerancia)
    else:
        polinomio = sp.simplify(sp.sympify(polinomio))
    if valores_coeficientes:
        return polinomio, coef_value
    else:
        return polinomio


if __name__ == '__main__':
    dados = np.loadtxt("dados9.txt", dtype=str, delimiter=';').transpose()
    # print(dados)

    equacoes = polinomio(dados, 1, em_decimais=False, tolerancia=None)
    print(equacoes)
    grafico_mtpl(experimental=dados, teorico=equacoes, exibir_plot=True, exibir_dados=True, exp_nome='Dados', teor_nome='Grau 2')
    x = sp.Symbol('x')

    lam_fx = sp.lambdify(x, equacoes, modules=["numpy"])
    eixo_y = lam_fx(5.4)
    print(eixo_y)
