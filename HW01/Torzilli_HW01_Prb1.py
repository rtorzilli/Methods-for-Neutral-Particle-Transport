# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:53:10 2017

@author: Robert
"""
import numpy as np
import matplotlib.pyplot as plt
# =============================================================================
# Note P(x)=f(xi)Li(x)
# =============================================================================

#Part C
#Given
xSet = [0,2,3,4]

def functionF (x):
    return(np.sin((np.pi*x)/2)+(x**2)/4)

#Used for plotting orginal values prior to interpolation
ySet = []
for xi in xSet:
    ySet.append(functionF(xi))

# Interpolation function using Lagrange Polynomials
def interpolateY (x,y, xInt):
    Li = 1
    yInterpolated = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if (i != j):
                processed = (xInt-x[j])/(x[i]-x[j])
                Li = Li * processed
        yInterpolated = yInterpolated+ Li * y[i]
        Li = 1
    return yInterpolated

#Interpolating over the given range
xInt = np.linspace(-.5,4.5,100)

def massInterpolate(xSet,ySet, xIntVals):
    yIntVals = []
    for xNew in xIntVals:
        yVal = interpolateY (xSet,ySet, xNew)
        yIntVals.append(yVal)
    return yIntVals

yInt = massInterpolate(xSet,ySet,xInt)

xSet2 = [0,1,2.5,4]
ySet2 =  []
for xi in xSet2:
    ySet2.append(functionF(xi))
yInt2 = massInterpolate(xSet2,ySet2, xInt)
    
#Plot
plt.plot(xSet,ySet, 'o', xInt,yInt, '-', color='r')
plt.plot(xSet2,ySet2, 'o', xInt, yInt2, '-', color = 'b')
plt.xlabel('X -Values')
plt.ylabel('Y- Values')
plt.title('Lagrange Polynomial Interpolation')
plt.grid(True)
plt.show