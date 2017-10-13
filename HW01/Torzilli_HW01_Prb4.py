# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:06:48 2017

@author: Robert
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#Part C solving for values k and P
#Given
E = [1.036126e-01,3.333834e-02,1.375409e-02,4.177237e-03,1.103962e-03,2.824698e-04,7.185644e-05,1.813937e-05]
h = [5.00000e-02,2.50000e-02,1.25000e-02,6.25000e-03,3.12500e-03,1.56250e-03,7.81250e-04,3.90625e-04]
n = len(h)

#From Numerical Methods, also x = h; y=E
Sxy = 0
Sxx = 0
for i in range(len(h)):
    Sxy = Sxy + h[i]*E[i]
    Sxx = Sxx + h[i]*h[i]
Sx = np.sum(h)
Sy=np.sum(E)

a1 = (n*Sxy-Sx*Sy)/(n*Sxx-Sx**2)
a0 = (Sxx*Sy-Sxy*Sx)/(n*Sxx-Sx**2)
myK = np.exp(a0)
print("Numerical Solution")
print("ln(k): "+ str(a0))
print("k: "+ str(myK) + " P: "+ str(a1))

#Part D find K and P using the curve_fit function
def err (h,k,p):
    return k*(h**p)

popt, pcov = curve_fit(err, h, E)
print("Pythons Curve Fit solution")
print("k: "+str(popt[0]) + " P: "+ str(popt[1]))

#Part E make a log-log and lin-lin plot that dispalys the input(h) and function (E or err)
#The Discussion is found on the PDF
fig1 = plt.figure()
plotLog = fig1.add_subplot(111)
plotLog.loglog(h,E)
fig2 = plt.figure()
plotLog = fig2.add_subplot(111)
plotLog.plot(h,E)