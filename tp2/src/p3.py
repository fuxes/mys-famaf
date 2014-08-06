# -*- coding: utf-8 -*-
import math
import random
import pylab
import numpy
from scipy import stats


def parametros_normal(v):
	X = math.fsum(v) / float(len(v))
	X2 = math.fsum(map(lambda x:x ** 2.0, v)) / float(len(v))
	S2 = X2 - X ** 2.0
	return X, S2

def parametros_lognormal(v):
	X = math.fsum(map(math.log, v)) / float(len(v))
	S2 = math.fsum(map(lambda x: (math.log(x) - X) ** 2.0, v)) / float(len(v))
	return X, S2

def parametros_gamma(v):
	X = math.fsum(v) / float(len(v))
	A = math.log(X) - math.fsum(map(math.log, v)) / len(v)
	alpha = 1.0 / (4*A) * (1.0 + math.sqrt(1.0 + 4.0/3.0 * A))
	lamb = alpha / X
	beta = 1.0 / lamb
	return alpha, beta

def graficar_normal(v):
	X, S2 = parametros_normal(v)
	print X, numpy.sqrt(S2)

	fig = pylab.figure()
	width = 0.35
	bins = [i for i in xrange(int(min(v)), int(max(v)) + 1)]
	pylab.hist(v, bins=bins, rwidth=width, align='right', normed=True, 
		label=u'Valores simulados', color='blue', histtype='bar')

	x = numpy.linspace(min(v),max(v),200)
	dist = stats.norm(loc=X, scale=numpy.sqrt(S2))
	pylab.plot(x, dist.pdf(x), color='red', label=u'Ajuste normal', 
		linewidth=2.0)

	pylab.ylim(0, 0.15)
	pylab.legend()
	pylab.title(u'Ajuste Normal')
	pylab.xlabel(u'Datos semanales')
	pylab.ylabel(u'Frecuencia Relativa')
	pylab.show()

	print "p-valor: %f" % kolmogorov_smirnov_normal(v, dist)


def graficar_lognormal(v):
	X, S2 = parametros_lognormal(v)
	print X, numpy.sqrt(S2)

	fig = pylab.figure()
	width = 0.35
	bins = [i for i in xrange(int(min(v)), int(max(v)) + 1)]
	pylab.hist(v, bins=bins, rwidth=width, align='right', normed=True, 
		label=u'Valores simulados', color='blue', histtype='bar')

	dist = stats.lognorm(numpy.sqrt(S2), scale=math.exp(X))
	x = numpy.linspace(min(v),max(v),200)
	pylab.plot(x,dist.pdf(x), color='red', label='Ajuste Lognormal',
		linewidth=2.0)

	pylab.ylim(0, 0.15)
	pylab.legend()
	pylab.title(u'Ajuste Lognormal')
	pylab.xlabel(u'Datos semanales')
	pylab.ylabel(u'Frecuencia Relativa')
	pylab.show()

	print "p-valor: %f" % kolmogorov_smirnov_lognormal(v, dist)


def graficar_gamma(v):
	alpha, beta = parametros_gamma(v)
	print alpha, beta

	fig = pylab.figure()
	width = 0.35
	bins = [i for i in xrange(int(min(v)), int(max(v)) + 1)]
	pylab.hist(v, bins=bins, rwidth=width, align='right', normed=True, 
		label=u'Valores simulados', color='blue', histtype='bar')

	dist = stats.gamma(alpha, scale=beta)
	x = numpy.linspace(min(v),max(v),200)
	pylab.plot(x,dist.pdf(x), color='red', label='Ajuste Gamma',
		linewidth=2.0)

	pylab.ylim(0, 0.15)
	pylab.legend()
	pylab.title(u'Ajuste Gamma')
	pylab.xlabel(u'Datos semanales')
	pylab.ylabel(u'Frecuencia Relativa')
	pylab.show()

	print "p-valor: %f" % kolmogorov_smirnov_gamma(v, dist)


def kolmogorov_smirnov_normal(muestra, dist):
    muestra.sort()
    n = len(muestra)
    
    # Calcular el estadístico D:
    d1 = max([float(j+1)/float(n) - dist.cdf(muestra[j]) for j in xrange(0, n)])
    d2 = max([dist.cdf(muestra[j]) - (float(j+1)-1.0)/float(n) for j in xrange(0, n)])
    d = max(d1, d2)

    # Calcular el valor p.
    p = 0
    r = 100
    for _ in xrange(r):
        v = dist.rvs(n)
        v.sort()
        Xsim, S2sim = parametros_normal(v)
        distSim = stats.norm(loc=Xsim, scale=numpy.sqrt(S2sim))
        D1 = max([float(j+1)/float(n) - distSim.cdf(v[j]) for j in xrange(0, n)])
        D2 = max([distSim.cdf(v[j]) - (float(j+1)-1.0)/float(n) for j in xrange(0, n)])
        D = max(D1, D2)
        if D >= d:
            p += 1

    return float(p) / float(r)


def kolmogorov_smirnov_lognormal(muestra, dist):
    muestra.sort()
    n = len(muestra)
    
    # Calcular el estadístico D:
    d1 = max([float(j+1)/float(n) - dist.cdf(muestra[j]) for j in xrange(0, n)])
    d2 = max([dist.cdf(muestra[j]) - (float(j+1)-1.0)/float(n) for j in xrange(0, n)])
    d = max(d1, d2)

    # Calcular el valor p.
    p = 0
    r = 100
    for _ in xrange(r):
        v = dist.rvs(n)
        v.sort()
        Xsim, S2sim = parametros_lognormal(v)
        distSim = stats.lognorm(numpy.sqrt(S2sim), scale=math.exp(Xsim))
        D1 = max([float(j+1)/float(n) - distSim.cdf(v[j]) for j in xrange(0, n)])
        D2 = max([distSim.cdf(v[j]) - (float(j+1)-1.0)/float(n) for j in xrange(0, n)])
        D = max(D1, D2)
        if D >= d:
            p += 1

    return float(p) / float(r)


def kolmogorov_smirnov_gamma(muestra, dist):
    muestra.sort()
    n = len(muestra)
    
    # Calcular el estadístico D:
    d1 = max([float(j+1)/float(n) - dist.cdf(muestra[j]) for j in xrange(0, n)])
    d2 = max([dist.cdf(muestra[j]) - (float(j+1)-1.0)/float(n) for j in xrange(0, n)])
    d = max(d1, d2)

    # Calcular el valor p.
    p = 0
    r = 1000
    for _ in xrange(r):
        v = dist.rvs(n)
        v.sort()
        alphaSim, betaSim = parametros_gamma(v)
        distSim = stats.gamma(alphaSim, scale=betaSim)
        D1 = max([float(j+1)/float(n) - distSim.cdf(v[j]) for j in xrange(0, n)])
        D2 = max([distSim.cdf(v[j]) - (float(j+1)-1.0)/float(n) for j in xrange(0, n)])
        D = max(D1, D2)
        if D >= d:
            p += 1

    return float(p) / float(r)

# Leer datos:
filename = "ganancia_media.dat"

f = open(filename, 'r')
v = []

for line in f:
	v.append(float(line))

graficar_normal(v)
graficar_lognormal(v)
graficar_gamma(v)