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
    yIntVals[:] = []
    for xNew in xIntVals:
        yVal = interpolateY (xSet,ySet, xNew)
        yIntVals.append(yVal)
    return yIntVals

yInt = massInterpolate(xSet,ySet,xInt)

#Part D new X values use same X Interpolate values
xSet2 = [0,1,2.5,4]
ySet2 =  []
for xi in xSet2:
    ySet2.append(functionF(xi))
yInt2 = massInterpolate(xSet2,ySet2, xInt)
    
# =============================================================================
# #Sanity check due to little change
# from scipy import interpolate
# LAG= interpolate.lagrange(xSet,ySet)
# yLAG = LAG(xInt)   
# LAG= interpolate.lagrange(xSet2,ySet2)
# yLAG2 = LAG(xInt)  
# =============================================================================
#Plot
mainPlot,(plt1,plt2) = plt.subplots(2,sharex=True, sharey= True)
plt1.plot(xSet,ySet, 'o')
plt1.plot( xInt,yInt, '-', color='r')
plt2.plot(xSet2,ySet2, 'o',color = 'm')
plt2.plot(xInt, yInt2, '-', color = 'g')
# =============================================================================
# #Plotting the Sanity check on the same 
# plt1.plot(xInt,yLAG, '--', color='k')
# plt2.plot(xInt, yLAG2, '--', color = 'k')
# =============================================================================
plt.xlabel('X -Values')
plt.ylabel('Y- Values')
plt.title('Lagrange Polynomial Interpolation')
plt.grid(True)
plt.show

#Checking the difference between the two yInterpolated sets
def percentDiff(old, new):
    if(old == 0):
        return 0
    try:
       return ((abs(new - old)/old))*100.0
    except ZeroDivisionError:
        return 0

maxChange = 0
minChange = 100
dataLocaMax = -1
dataLocaMin = -1
for i in range(len(yInt)):
    change = percentDiff(yInt[i], yInt2[i])
    if (maxChange<change):
        dataLocaMax = i
        maxChange = change 
    if (minChange>change):
        dataLocaMin = i
        minChange = change 
print("Min Change: " + str(minChange) + "% Located at: " + str(dataLocaMin))
print("Max Change: " + str(maxChange) + "% Located at: " + str(dataLocaMax))
    

