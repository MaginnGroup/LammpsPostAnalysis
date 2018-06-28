# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:16:20 2015

@author: mhumbert
"""

from lammpsio import LammpsLog
import numpy as np

trjlen = 1500000
trjskip = 100001
numtrj = 60




Log = LammpsLog.from_file('test_1/visc.log')
minnum = trjlen-trjskip
(Time,visco)=Log.viscosity(trjskip)
viscosity = np.zeros((numtrj,minnum))
average = np.zeros(minnum)
stddev = np.zeros(minnum)
for i in range(0,len(visco)):
    viscosity[0][i] += visco[i]
if len(visco) < minnum:
    minnum = len(visco)


for i in range(2,numtrj+1):
    print i
    Log = LammpsLog.from_file('test_{0}/visc.log'.format(i))
    (Time,visco)=Log.viscosity(trjskip)
    for j in range(0,len(visco)):
        viscosity[i-1][j] += visco[j]
    if len(visco) < minnum:
        minnum = len(visco)

for i in range(0,minnum):
    average[i] = np.average(viscosity.transpose()[i])
    stddev[i] = np.std(viscosity.transpose()[i])

output = open('average_viscosity','w')
for i in range(0,minnum):
    output.write('{0}\t{1}\t{2}\n'.format(Time[i],average[i],stddev[i]))
output.close()
