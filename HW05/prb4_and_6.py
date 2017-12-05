# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:19:59 2017

@author: Robert
"""
import matplotlib.pyplot as plt
import numpy as np
from copy import copy

# Given values
# Boundary condition
a=4.0
# first source term assuming its the same for everything
S0 = 8.0
# Assumption homogeneneous, uniform mesh thus h, D, and macroAbs are constant
hVals=[.1,1,.5,.1,.05,.01]
D=1.0
macroAbs=.2

# To calculate relative error later
def relError (xOld, xNew):
    if(xNew==0):
        return 0
    #out = np.linalg.norm(xNew-xOld, 1)/np.linalg.norm(xNew, 1)
    out = abs(xNew-xOld)/abs(xNew)
    return out

# What we will compare to (wolfram to solve the integral from -a to a)
phiAna = 8.02236

# Problem calls for the use of the finite diff and Gaussian elimination
# Use finite diff to create matrix A and Gaussian elimination to solve 
# Ax=b

# Finite difference for a homogenerous uniform mesh which I am assuming
def finiteDiff(a,h,D,sigma):
    n = len(a)
    aNew = copy(a)
    # first row
    for i in range(n):
        if i == 0:
            aNew[i,i] = 2*D/(h**2)+sigma
            aNew[i,i+1] = -(2*D/(h**2))
            #built in python funciton
            #diags([value],[i-1,i,i+1])
        if i == n-1:
            aNew[i-1]=-D/(h**2)
            aNew[i]= 2*D/(h**2)+sigma
        else:
            aNew[i,i-1] = -D/(h**2) 
            aNew[i,i] = 2*D/(h**2)+sigma
            aNew[i,i+1] = -D/(h**2) 
    return aNew
    
def thomas(A, b):
    # Set up variables
    n= np.size(b)
    u =np.zeros(n)
    v=np.zeros(n)
    
    #soultion vector
    phi = np.zeros(n)
    
    # 1 set B0 S0
    u[0]=A[0,0]
    v[0]=b[0]
    
    # 2 
    for i in range(1,n):
        u[i]=A[i,i]-(A[i,i-1]*A[i-1,i])/(u[i-1])
        v[i] = b[i]-(A[i,i-1]*v[i-1])/(u[i-1])
    # 3 reverse that loop
    phi[n-1] = u[n-1]/v[n-1]
    for i in range(n-2,0,-1):
        phi[i] = (v[i]-A[i,i+1])/(u[i])
    return phi

for h in hVals:
    n=len(np.arange(-4,4,h))
    
    zeroA = np.zeros((n,n),float)
    A = finiteDiff(zeroA,h,D,macroAbs)    
    s = np.full((n,1),S0)
    phi = thomas(A,s)    
    
    relativeError=[0]
    for i in range(n):
        relativeError.append(relError(phiAna,phi[i]))
    print('Max Error for h = '+str(h)+' is :'+str(max(relativeError)))
    
    # plot results for Phi(x)vs x
    
    xAxis = np.arange(-4,4,h)
    yAxis = copy (phi)
    # Plotting:
    figureFile = plt.figure()
    plt.rcParams.update({'font.size': 10})
    plt.errorbar(xAxis, # X-Axis
                 yAxis, # Y-Axis
                 label='Calculted',
                 color='k',
                 # Markers:
                 marker='^',
                 markersize=10,
                 markeredgecolor='r',
                 # Error Bars:
                 capsize=10, # error bar capsize
                 capthick=1,
                 ecolor='r')
    
    plt.legend(loc='upper right',prop={'size': 8})
    plt.xlabel('x')
    plt.ylabel('phi(x')
    plt.title('Ax=b solution using numerical analysis')
    plt.show