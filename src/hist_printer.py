import algorithm as x
import alg_2op as y
import alg_3rep as z
import matplotlib.pyplot as plt

if __name__ == "__main__":
    a = []
    b = []
    c = []
    for _ in range(10000):
        a.append(x.experimento(5, 2, 1, 0.125))
        b.append(y.experimento(5, 2, 1, 0.125))
        c.append(z.experimento(5, 3, 1, 0.125))

    params = dict(bins=30, normed=True, alpha=0.5, range=(0,10))
    plt.axis([0, 10, 0, 0.4])
    plt.subplot(312)
    plt.subplots_adjust(hspace=.4)
    """
    plt.hist(a, **params)
    plt.hist(b, **params)
    plt.hist(c, **params)
    plt.figure() # crea uno nuevo
    # agrgar legend a casa caso
    add yticks
    add better conclusions
    """
    plt.hist((a, b, c), **params)
    plt.legend(["Un tecnico y dos repuestos","Dos tecnicos y dos repuestos", "Un tecnico y tres repuestos"], fontsize=9)
    plt.title('Comparacion')
    plt.xlabel('Tiempo de falla del sistema')
    plt.ylabel('Proporcion de falla')
    plt.savefig('../img/comparisson.png', bbox_inches='tight', figsize=(8.0,5.0))
    plt.show()
