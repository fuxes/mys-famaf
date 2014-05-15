import random
import math

inf = float("inf")
# ipython notebook + matplotlib (o gnuplot)
def experimento(N, S, Tf, Tr):
    t = 0
    r = 0
    t1_ = inf
    t2_ = inf
     
    exponencial = (lambda x: -math.log(random.random()) * x)
    events = [exponencial(Tf) for _ in range(N)]
    events.sort()

    while True:
        if (events[0] < t1_ and events[0] < t2_): # Caso 1: Falla una maquina (mqn)
            t = events[0]
            r += 1
            if (r == S+1): # Mqs rotas > Repuestos
                return t;
            else:
                x = exponencial(Tf)
                events[0] = t + x # tiempo en el q se rompe el repuesto
                events.sort()
                if (t1_ == inf): # op1 idle
                    t1_ = t + exponencial(Tr)
                    continue
                if (t2_ == inf): # op2 idle
                    t2_ = t + exponencial(Tr)

        elif (events[0] >= t1_): # op1 ends
            t = t1_
            r -= 1
            if ((r > 1 and t2_ != inf) or (t2_ == inf and r > 0)):
                t1_ = t + exponencial(Tr)
            else: # Si no, operario inactivo
                t1_ = inf

        elif (events[0] >= t2_): # op2 ends
            t = t2_
            r -= 1
            if ((r > 1 and t1_ != inf) or (t1_ == inf and r > 0)):
                t2_ = t + exponencial(Tr)
            else: # Si no, operario inactivo
                t2_ = inf

if __name__ == "__main__":
    for N in [100, 1000, 10000]:
        t = 0
        for _ in range(N):
            t += experimento(5, 2, 1, 0.125)
        e = t / float(N)

        s = 0
        for _ in range(N):
            t = experimento(5, 2, 1, 0.125) - e
            s += t * t
        v = s/float(N-1)
        print "Esp: " + str(e) + " - Var: " + str(v)


