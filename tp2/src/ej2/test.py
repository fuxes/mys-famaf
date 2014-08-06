import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cumfreq

P = 0.4
Q = 1 - P 

a = np.random.geometric(P, size=1000)
b = np.random.geometric(P, size=1000)
c = np.random.geometric(P, size=1000)

common_params = dict(bins=[x for x in range(1,14)], normed=1, range=(0,15))

plt.title('Histograma comparativo de simulaciones y probabilidad teorica')
plt.ylabel('Frecuencia relativa')
plt.xlabel('Valores')
plt.hist([a, b, c], **common_params)

gteo = [P * pow(Q, i-1) for i in range(1,14)]
g = cumfreq(gteo, 15)



plt.show()

