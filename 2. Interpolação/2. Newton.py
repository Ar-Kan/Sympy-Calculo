import numpy as np
import sympy as sp
from grafico_interpolacao import grafico_mtpl


def diferenca_Dividida(x0, x1, y0, y1):
    ans = sp.nsimplify((sp.sympify(y1) - sp.sympify(y0)) /
                       (sp.sympify(x1) - sp.sympify(x0)))
    if ans == "zoo":
        return np.nan
    else:
        return ans


def forma_Diferencas(valores):
    r'''
    Funcao que recebe os valores de X e Y em forma de matriz,
    retornando uma matriz com as diferencas divididas.

    Entrada simbolica:
        [['X0' 'X1' 'X2' ... 'Xn']
         ['Y0' 'Y1' 'Y2' ... 'Yn']]
    Entrada numerica:
        [['-1' '0' '1' '2']
         ['1' '1' '0' '-1']]
    ---
    Saida simbolica:
        [['X0' 'X1' 'X2' ... 'Xn']
         ['Y0' 'Y1' 'Y2' ... 'Yn']
         ['f[X0, X1]' ... 'f[Xn-1, Xn]']
         [...]
         ['f[X0, ..., Xn]']]
    Saida numerica:
        [['-1'   '0'   '1'    '2']
         ['1'    '1'   '0'   '-1']
         ['0'   '-1'  '-1'  'nan']
         ['-1/2' '0'  'nan' 'nan']
         ['1/6' 'nan' 'nan' 'nan']]
    '''
    tamanho = len(valores[0])
    i = 2
    n = 1
    disloc = 1
    while True:
        valores = np.append(valores, [np.empty(tamanho) * np.nan], axis=0)
        matriz = list(map(diferenca_Dividida,
                          valores[0], valores[0][disloc:],
                          valores[n], valores[n][1:]))
        for pos in range(len(matriz)):
            valores[i][pos] = matriz[pos]
        i += 1
        n += 1
        disloc += 1
        if len(matriz) == 1:
            break
    return valores


def interpolacao_Newton(matriz, tolerancia=None, saida_latex=False):
    r'''
    Funcao que recebe os valores de X e Y em forma de matriz,
    com a funcao forma_Diferencas cria uma matriz para com
    os valores de interpolacao.
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
    matriz = forma_Diferencas(matriz)
    print(matriz)
    polinomio = ""
    termo = ""
    for n in range(1, len(matriz)):
        fx = matriz[n][0]
        for i in range(n - 1):
            Xn = matriz[0][i]
            termo += "(x-({}))".format(Xn)
            if i < (n - 2):
                termo += "*"
        polinomio += "({}".format(fx)
        if len(termo) > 0:
            polinomio += "*{})".format(termo)
        else:
            polinomio += ")"
        if n < len(matriz) - 1:
            polinomio += "+"
            termo = ""
    x = sp.Symbol('x')
    print(polinomio)
    polinomio = sp.simplify(sp.sympify(polinomio))
    polinomio = sp.nsimplify(polinomio, tolerance=tolerancia)
    if saida_latex:
        return sp.latex(polinomio)
    else:
        return polinomio


if __name__ == "__main__":

    dados = np.loadtxt("dados7.txt", dtype=str, delimiter=';')
    dados = dados.transpose()
    equacao = interpolacao_Newton(dados, tolerancia=None)
    # print(equacao)
    # grafico_mtpl(equacao, dados)

    print(dados.astype(np.float))
    print(sp.latex(equacao))
