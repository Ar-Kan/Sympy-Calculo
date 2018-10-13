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


def grafico_mtpl(experimental=None, teorico=None,
                 exibir_plot=False, exibir_dados=False,
                 exp_nome=None, teor_nome=None):
    experimental = experimental.astype(np.float)
    plt.grid(True, linestyle=':')
    plt.axhline(0, color='k')
    plt.axvline(0, color='k')
    if exibir_dados:
        if experimental is not None and not exp_nome:
            plt.scatter(experimental[0], experimental[1],
                        label=None, marker='o', c='magenta')
        elif experimental is not None and exp_nome:
            experimental = experimental.astype(np.float)
            plt.scatter(experimental[0], experimental[1],
                        label=exp_nome, marker='o', c='magenta')
    if teorico is not None:
        x = sp.Symbol('x')
        lam_fx = sp.lambdify(x, teorico, modules=["numpy"])
        eixo_x = np.linspace(experimental[0][0],
                             experimental[0][-1], num=1000)
        eixo_y = lam_fx(eixo_x)
    if not teor_nome and teorico is not None:
        plt.plot(eixo_x, eixo_y, label=None)
    elif teor_nome and teorico is not None:
        plt.plot(eixo_x, eixo_y, label=teor_nome)
    if exp_nome or teor_nome:
        plt.legend(prop={'size': 10}, framealpha=1)
    if exibir_plot:
        plt.show()
