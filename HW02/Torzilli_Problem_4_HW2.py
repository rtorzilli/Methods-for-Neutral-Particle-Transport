# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:05:19 2017

@author: Robert
"""
import numpy as np
import matplotlib.pyplot as plt
# Write a function for Composite Simpson's 3/8 rule to compute the given 
# integral

# =============================================================================
# This function only works for a predetermined integral
# botBound and topBound are the endpoints of the integral
# n is the number of points to use in the integration (divisble by 3)
# =============================================================================
def givenIntegral(x):
    if (np.abs(x) != 1):
        Fx = x/(np.sqrt((x**2)-1))
    else :
        return print("Attempted to divide by zero")
    return Fx
def compositeSimpson3_8(botBound, topBound, n, function):
    if ((n%3 == 0)):
        Fvalues = [None]*(n+1)
        h = (topBound-botBound)/n
        #Gather funciton values for simpson
        for i in range(1,n):
            Fvalues[i] = function(botBound+h*i) 
        Fvalues[0] = function(botBound)
        Fvalues[n] = function(topBound)
        if (n>=6):
            # Full method  
            sum3 = 0
            sum2 = 0
            for i in range(1,n,3):
                sum3 += (Fvalues[i]+Fvalues[i+1])
            for i in range(3,n-1,3):
                sum2 += Fvalues[i]
            I = (3*h/8)*(Fvalues[0]+3*sum3+2*sum2+Fvalues[n])
        else :
            # We know that only n = 3 will make it to this block so use 
            # approximated simpsons 3/8
            I = (3*h/8)*(Fvalues[0]+3*(Fvalues[1]+Fvalues[2])+Fvalues[n])
    else :
        print("The number of points to integrate over must be divisible by 3" + 
              " and at least 6")
    return I
integrateI = compositeSimpson3_8(2,4,3,givenIntegral)
print(integrateI)
integrateI = compositeSimpson3_8(2,4,6,givenIntegral)
print(integrateI)
# Experimentally dermine the rate of convergence as a function of h
# =============================================================================
# Recall that h will only change based on the subintervals we specify
# Note that the norm used to calculate the rate of convergence has not
# been specified. We will choose the infinite norm
# =============================================================================
I = []
u = []
k = []
#From part A
xReal = np.sqrt(15)-np.sqrt(3)
for n in range(3,1000,3):
    I.append(compositeSimpson3_8(2,4,n,givenIntegral))
for i in range(1,len(I)):
    u.append((np.linalg.norm([I[i]-xReal],np.inf))/(np.linalg.norm([I[i-1]-xReal],np.inf)))
    k.append(i)
plt.plot(k,u,'-ro')
plt.xlabel("Iteration")
plt.ylabel("Rate of Convergence")
plt.title("Rate of Convergence as Iteration goes to 333")

# =============================================================================
# As we can see the rate of convergence (u) goes to one this also indicates that 
# the convergence is sublinear
# =============================================================================
