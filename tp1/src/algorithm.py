import random
import math

# ipython notebook + matplotlib (o gnuplot)
def experimento(N, S, Tf, Tr):
    t = 0
    r = 0
    t_ = float("inf")
     
    exponencial = (lambda x: -math.log(random.random()) * x)
    events = [exponencial(Tf) for _ in range(N)]
    events.sort()

    while True:
        if (events[0] < t_): # Caso 1: Falla una maquina (mqn)
            t = events[0]
            r += 1
            if (r == S+1): # Mqs rotas > Repuestos
                return t;
            else:
                x = exponencial(Tf)
                events[0] = t + x # tiempo en el q se rompe el repuesto
                events.sort()
                if (t_ == float("inf")): # op idle == r=1
                    t_ = t + exponencial(Tr)

        else: # Caso 2: Se repara una mqn
            t = t_
            r -= 1
            if (r > 0): # Si hay, arreglar sig mqn
                t_ = t + exponencial(Tr)
            else: # Si no, operario inactivo
                t_ = float("inf")

if __name__ == "__main__":
    x = []
    for N in [100, 1000, 10000]:
        t = e = 0
        for _ in range(N):
            t = experimento(5, 2, 1, 0.125)
            if (N == 10000):
                x.append(t)
            e += t 
        e = e / float(N)

        s = 0
        for _ in range(N):
            t = experimento(5, 2, 1, 0.125) - e
            s += t * t
        v = pow(s/float(N-1), 0.5)
        print "Esp: " + str(e) + " - Var: " + str(v)

        if (N == 10000):
            import matplotlib.pyplot as plt
            plt.hist(x, 50, normed = 1, facecolor='b', alpha=0.5, range=(0,15))
            plt.ylim(0,0.6)
            plt.xticks([0,0.5,1,1.5,2,3,5,7.5,10], fontsize=10, rotation='vertical')
            plt.xlabel('Tiempo de falla del sistema', fontsize=10)
            plt.ylabel('Proporcion de falla', fontsize=10)
            plt.legend(["Un tecnico y dos repuestos"], fontsize=10)
            plt.savefig('../img/1op2rep.png', bbox_inches='tight')
            plt.show()
