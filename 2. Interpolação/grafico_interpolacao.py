import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
try:
    from matplotlib import style
    try:
        style.use('seaborn-paper')
    except:
        style.use('ggplot')
except:
    pass


def grafico_mtpl(func, dados):
    '''
    Nao aceita funcoes em LaTeX
    '''
    dados = dados.astype(np.float)
    x = sp.Symbol('x')
    lam_fx = sp.lambdify(x, func, modules=["numpy"])
    eixo_x = np.linspace(dados[0][0], dados[0][-1], num=1000)
    eixo_y = lam_fx(eixo_x)

    tex_titulo = "${}$".format(sp.latex(func))
    plt.title("Interpolacao Newton")
    plt.grid(True, linestyle=':')
    plt.axhline(0, color='k')
    plt.axvline(0, color='k')
    plt.scatter(dados[0], dados[1], label=None,
                marker='o', color='r')
    plt.plot(eixo_x, eixo_y, label=tex_titulo, color='b')
    plt.legend(prop={'size': 10}, framealpha=1)
    axes = plt.gca()
    axes.set_xlim(np.amin(eixo_x), np.amax(eixo_x))
    axes.set_ylim(np.amin(eixo_y), np.amax(eixo_y))
    plt.show()
