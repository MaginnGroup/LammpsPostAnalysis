# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:05:34 2016

@author: mhumbert
"""

import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt

def doubexp(x,A,alpha,tau1, tau2):
    return A*alpha*tau1*(1-np.exp(-x/tau1))+A*(1-alpha)*tau2*(1-np.exp(-x/tau2))
    
filename = 'average_viscosity'

time = np.genfromtxt(filename, usecols = 0)
visc = np.genfromtxt(filename, usecols = 1)
stddev = np.genfromtxt(filename, usecols = 2)
popt2=[1e-3,1.5e-1,3e4,1e3]

foundcutoff = False
cut = 1
while not foundcutoff and cut<len(visc):
    if stddev[cut] > 0.4*visc[cut]:
        foundcutoff = True
    else:
        cut += 1
#cut = len(visc)
popt2,pcov2 = optimize.curve_fit(doubexp, time[50:cut], visc[50:cut],maxfev=1000000,p0=popt2, sigma=stddev[50:cut])

plt.plot(time[:cut],visc[:cut])
plt.plot(time[:cut],doubexp(time[:cut],*popt2))
plt.plot(time[:cut],stddev[:cut])
plt.show()
print 'viscosity: {0}'.format(popt2[0]*popt2[1]*popt2[2]+popt2[0]*(1-popt2[1])*popt2[3])
