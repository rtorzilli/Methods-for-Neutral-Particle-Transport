# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 07:36:05 2017

@author: Robert
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

#Given
x= [1,2,3,4,5,6,7]
y = [1,4,10,12,5,4,0]

#Interpolate piecewise
PIL = interpolate.interp1d(x, y)
xPIL = np.arange(1, 6, 0.05)
yPIL = PIL(xPIL)   

#Interpolate with Lagrange
LAG= interpolate.lagrange(x,y)
xLAG = np.arange(.75, 6.25, 0.05)
yLAG = LAG(xLAG)   

#Interpolate with Spline 
Spline= interpolate.splrep(x,y)
xSpline = np.arange(.75, 6.25, 0.05)
ySpline = interpolate.splev(xSpline,Spline,der=0)  

#Plot all on same using subplots
mainPlot,(plotPIL,plotLPI,plotSI) = plt.subplots(3,sharex=True, sharey= True)
plotPIL.plot(x, y, 'o', xPIL, yPIL, '-', color= 'r')
plotLPI.plot(x, y, 'o', xLAG, yLAG, '-', color = 'g')
plotSI.plot(x, y, 'o', xSpline, ySpline, '-')
plt.show()