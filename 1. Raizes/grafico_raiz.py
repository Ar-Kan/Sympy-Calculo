import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

try:
    from matplotlib import style
    try:
        style.use('seaborn-paper')
    except:
        style.use('ggplot')
except:
    pass


def grafico_mtpl(func, f_raiz):
    x = sp.Symbol('x')
    fn_raiz = float(f_raiz)
    np_limite = abs(fn_raiz) + 20
    lam_x = sp.lambdify(x, func, modules=['numpy'])
    eixo_x = np.linspace(-np_limite, np_limite, num=1000)
    eixo_y = lam_x(eixo_x)

    tex_titulo = "${}$".format(sp.latex(func))  # "$"+latex(func)+"$"
    plt.title("Newton-Raphson")
    plt.grid(True, linestyle=':')
    plt.axhline(0, color='k')
    plt.axvline(0, color='k')
    plt.plot(eixo_x, eixo_y, label=tex_titulo)
    plt.scatter(fn_raiz, 0, label=str(f_raiz), color='r', marker='o')
    plt.legend()
    axes = plt.gca()
    axes.set_xlim([eixo_x[0], eixo_x[-1]])
    axes.set_ylim([eixo_x[0], eixo_x[-1]])
    plt.show()
