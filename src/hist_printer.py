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

    params = dict(bins=40, normed=True, alpha=0.5, range=(0,15))
    #plt.hist(x, 50, normed = 1, facecolor='b', alpha=0.5, range=(0,15))
    #plt.axis([0, 10, 0, 0.4])
    #plt.subplot(312)
    plt.subplots_adjust(hspace=.4)
    plt.ylim(0,0.6)
    plt.xticks([0,0.5,1,1.5,2,3,5,7.5,10], fontsize=10, rotation='vertical')
    plt.yticks(fontsize=10)
    plt.hist((a, b, c), **params)
    plt.legend(["Un tecnico y dos repuestos","Dos tecnicos y dos repuestos", "Un tecnico y tres repuestos"], fontsize=9)
    plt.xlabel('Tiempo de falla del sistema', fontsize=10)
    plt.ylabel('Proporcion de falla', fontsize=10)
    plt.title('Comparacion')
    plt.savefig('../img/comparisson.png', bbox_inches='tight', figsize=(2,20))
    plt.show()
