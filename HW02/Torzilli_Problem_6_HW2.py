# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:49:19 2017

@author: rober
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
nuclearData = {# Np cascade half life    branching ratio, energy (not needed)
   'Fr-221' : (       288, [('At-217', u"\u03B1",       1.000, 6.300)]),
   'At-217' : (     32e-3, [('Bi-213', u"\u03B1",       1.000, 7.000)]),
   'Bi-213' : (      2790, [('Po-213', u"\u03B2\u207B", 0.978, 1.423), ('Tl-209', u"\u03B1", 0.022, 5.870)]),
   'Po-213' : (   3.72e-6, [('Pb-209', u"\u03B1",       1.000, 8.536)]),
   'Tl-209' : (       132, [('Pb-209', u"\u03B2\u207B", 1.000, 3.990)]),
   'Pb-209' : (     11700, [('Bi-209', u"\u03B2\u207B", 1.000, 0.644)]),
   'Bi-209' : (5.9918E+26, [('Tl-205', u"\u03B1",       1.000, 3.137)]),
   'Tl-205' : (    np.inf, []),
  }
# Create a list with all the keys
caller = list(nuclearData.keys())
#Key Value
print(caller[2])
#Branch Ratio
print(nuclearData[str(caller[2])][1][1][2])
#HalfLife
print(nuclearData[str(caller[2])][0])
#Key Value
print(caller[4])
#Branch Ratio
print(nuclearData[str(caller[4])][1])
#HalfLife
print(nuclearData[str(caller[4])][0])

def equ(N,t,halflife,prevN = 0, minus = -1,prevDC = 0):
    decayConstant = (np.log(2))/halflife
    dNdT=minus*decayConstant*(N*np.exp(-decayConstant*t))+prevDC*(prevN*np.exp(-decayConstant*t))
    return dNdT
time = np.arange(0,24*60*60)
# Assume an intital value of 100 
populationN =[]
for i in caller:
    # No parent so only decay
    if (i == 'Fr-221'):
        populationN.append(odeint(equ,100,time,(nuclearData[str(i)][0],)))
    # No child so no deacy
    elif (i == 'Tl-205'):
        populationN.append(odeint(equ,100,time,(nuclearData[str(i)][0],)))
    # Parent and Child
    else:
        populationN.append(odeint(equ,100,time,(nuclearData[str(i)][0],)))        
    previous = i
plt.plot(time,populationN[0],'r')
plt.plot(time,populationN[2],'c')
plt.plot(time,populationN[3],'m')
plt.plot(time,populationN[3],'y')
plt.plot(time,populationN[4],'k')
plt.plot(time,populationN[5],'g')
plt.plot(time,populationN[6],'b')
plt.plot(time,populationN[7],'*')
plt.xlabel("Time in Seconds")
plt.ylabel("Population N")
plt.title("N vs Time :: Showing Decay")