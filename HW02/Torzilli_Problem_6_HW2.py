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

# =============================================================================
# An attempt at making a unified funciton where the optional args allow the 
# calculation of the Parent, Daughter, GrandDaughter by slightly changing the working
# equation. Does not work well for this problem or with the ODEINT since that function 
# seems to ignore when the values are changed.
# =============================================================================
def equ(N,t,halflife,prevN = 0, minus = -1,prevDC = 0):
    decayConstant = (np.log(2))/halflife
    dNdT=minus*decayConstant*(N*np.exp(-decayConstant*t))+prevDC*(prevN*np.exp(-decayConstant*t))
    return dNdT
# Time interval of 1 sec to 1 day
time = np.arange(0,24*60*60)
# Assume an intital value of 1000 
populationN =[]
for i in caller:
    N0 = 1000
    # No parent so only decay
    if (i == 'Fr-221'):
        populationN.append(odeint(equ,N0,time,(nuclearData[str(i)][0],)))
    # No child so no deacy
    elif (i == 'Tl-205'):
        populationN.append(odeint(equ,N0,time,(nuclearData[str(i)][0],)))
    # Parent and Child
    else:
        populationN.append(odeint(equ,N0,time,(nuclearData[str(i)][0],)))        
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

# =============================================================================
# Comment on what happens if you start higher in the decay series. What about 
# if you carry the decay to longer times?
# =============================================================================

# =============================================================================
# We would expect the population of atoms to last longer since it would take longer
# for it to decay completly to zero again.
# 
# We would expect to see oscillations as well as a bigger picture of what occurs
# when each atom decayed
# 
# WE don't here since the code is incomplete and neglects the parent relationship
# that would cause this
# =============================================================================

# =============================================================================
# If you carry the decay far enough in time, you start to see oscillations in 
# the population. Comment on the cause of these oscillations.
# =============================================================================

# =============================================================================
# The oscillations I would assume are caused by the previous Isotopes differing
# halflifes and decay constants. 
# =============================================================================
