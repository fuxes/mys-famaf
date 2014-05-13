import random
import math

# ipython notebook + matplotlib (o gnuplot)

def exponencial(l):
    u = random.random() 
    t = float(((-1.0) / float(l)) * math.log(u))
    return t

def eventos(n, l):
    t = []
    for _ in range(n):
        x = float(exponencial(l))
        t.append(x)
    return t

def experimento(N, S, Tf, Tr):
    t = 0
    r = 0
    t_ = float("inf")
    
    xs = eventos(N, Tf) # Genera la lista de eventos
    xs.append(t_)
    xs.sort()

    while True:
        if (xs[0] < t_): # Caso 1: Falla una maquina (mqn)
            t = xs[0]
            r += 1
            if (r == S+1): # Mqs > Repuestos
                return t;
            else:
                x = exponencial(Tf)
                xs[0] = t + x # Se vuelve a romper en t+x
                xs.sort()
                if (r == 1): # operario emp a trabajar
                    t_ = float(t + exponencial(1 / float(Tr)))

        else: # Caso 2: Se repara una mqn
            t = t_
            r -= 1
            if (r > 0): # Si hay, arreglar sig mqn
                t_ = float(t + exponencial(1/float(Tr)))
            else: # Si no, operario inactivo
                t_ = float("inf")

if __name__ == "__main__":
    t = 0
    for N in [100, 1000, 10000]:
        for _ in range(N):
            t += experimento(5, 2, 1, 0.125)
        print t / float(N)
