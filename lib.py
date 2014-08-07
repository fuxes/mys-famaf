import math
import random
import numpy

"""
INTEGRACION POR MONTE CARLO
"""

# Integ en (a,b)
mc1 = lambda g,y: (b-a) * g(a+(b-a)*y)

# Integ en (0,inf)
mc2 = lambda g,y: g(1/float(y) - 1) / float(y*y)

# Integ en (-inf, inf)
	# Si la fc es par: 2 * int(0,inf) f(x) dx
	# Si no es par partir: 
	# (0,inf) y cambio de variables a [0,1]
	# int(-inf,0) f(x) dx = int(0, inf) f(-x) dx = int(0,1) f(1-float(y))/ float(y*y) dx
mc3 = lambda g,y: g(1 - 1/float(y)) / float(y*y)

"""
VARIABLES ALEATORIAS DISCRETAS
Si se puede usar numpy: http://docs.scipy.org/doc/numpy/reference/routines.random.html
"""
# Uniforme en (a,b)
unif = lambda a,b: math.floor(random.random() * b)+ a

#Permutacion aleatoria de A
shuffle = lambda a: random.shuffle(a)

#Promedio sumatoria
def prom(g, a, b, N=100, T=10000):
	S = 0
	for _ in range(N):
		S += g(unif(a,b))
	S *= (T/N)
	return S

# VA Geom
geom = lambda p: math.floor(math.log(random.random()) / math.log(1-p)) + 1

#VA Poisson
def poisson(lamb):
	i = 0
	p = math.exp(-lamb)
	F = p
	u = random.random()
	while (u >= F):
		p = lamb * p / float(i+1)
		F += p
		i += 1
	return i

# exp con rate lamb
expva = lambda l: -1/float(l) * math.log(random.random()) 

# Returns 2 Normals VAs
def twoStandardNormals():
	s = 1
	while (s > 1):
		u = random.random()
		v = random.random()
		x = 2 * u - 1 
		y = 2 * v - 1
		s = x * x + y * y
	p = math.sqrt(-2 * math.log(s) / float(s))
	return p * x, p * y

"""
Metodos
"""
# Inverse transform algorithm
"""
X = F^-1(U) then x = F(x) = x^n => despejar x
"""

# Aceptacion y rechazo
def ayr(q, p, c):
	t = True
	while (t):
		Y = q()
		u = unif(0,1)
		t = (u < p(Y)/float(c * q(Y)))
	return Y

"""
GEN PROC DE Poisson
"""
# T Time units of Poisson Proccess w/ Rate Lambd
def poissonProccess(lamb, T):
	t = 0
	s = []
	while (t <= T):
		u = random.random()
		t -= 1/float(lamb) * math.log(u)
		s.append(t)
	return s

# T time units of a Nonhomogeneous Poisson Process
def nonhomogeneousPoissonProccess(lamb, T, flamb):
	t = 0
	s = []
	while (t <= T):
		u = random.random()
		t -= 1/float(lamb) * math.log(u)
		y = random.random()
		if (y <= flamb(t) / float(lamb)):
			s.append(t)
	return s