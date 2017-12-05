# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:40:41 2017

@author: Robert
"""

import numpy as np
from copy import copy

# Problem 2 Start

# Problem given values
n=5
w=1.15
Xo = 0.0

# Probelem inferred values
D=3
bGiven=100.0
allowedTol = 1.0E-6

# Create matrix A with given n
A = np.zeros((n,n),float)
np.fill_diagonal(A,D)
for i in range(n-1):
    A[i][i+1]=-1
for i in range(1,n):    
    A[i][i-1]=-1

# Create Solution Matrix
xk = np.full((n,1),Xo)

# Create b matrix
b = np.full((n,1),bGiven)

# Convergeence
def converge(xOld,xNew):
    convVal =np.linalg.norm(xOld-xNew, 2)/np.linalg.norm(xNew, 2)
    return convVal

# Jacobi Method, pass in a Matrix, Solution, sum end point, and first X value
def jacobi(A,b,x,i):
    # Go one more since Python doesnd do last step
    n=len(x)
    # Reset each round
    Y =0.
    Z =0.
    c=1./A[i,i]
    X = b[i]
    for j in range(0,i):
        Y += A[i,j]*x[j]
    for j in range(i+1,n):
        Z += A[i,j]*x[j]
    xSol=(X-Y-Z)*c
    return xSol

# Consider this a test for Jacobi
tol = [1]
# just to initialize
xNewJac= copy(xk)
iteration=0
# Index last value in tolerance
while tol[-1]>allowedTol:
    xOldJac=copy(xNewJac)
    iteration+=1
    for i in range(n):
       xNewJac[i] = jacobi(A,b,xOldJac,i)
    tol.append(converge(xOldJac,xNewJac))    
print('Jacobi iterations: '+str(iteration))
print('Jacobi Solution Vector')
print(xNewJac)
print('Tolerance met at: '+str(tol[-1])+'\n')
	
#! Fauss Seidel Method for solving
def GSI (A,b,x,i):
    n=len(x)
    # Reset each round
    Y =0.
    Z =0.
    c=1./A[i,i]
    X = b[i]
    
    xOld=copy(x)
    xNew=copy(x)
    for j in range(0,i):
        # Last value in the old is the "new" value of the iteration
        Y += A[i,j]*xNew[j-1]
    for j in range(i+1,n):
        Z += A[i,j]*xOld[j]
    xNew=(X-Y-Z)*c
    return xNew

# Consider this a test for Gauss Siedel 
tol = [1]
xNewGauss= copy(xk)
iteration=0
while tol[-1]>allowedTol:
    iteration+=1
    xOldGauss=copy(xNewGauss)
    for i in range(n):
        xNewGauss[i] = GSI(A,b,xOldGauss,i)
    tol.append(converge(xOldGauss,xNewGauss))
print('GSI iterations: '+str(iteration))
print('GSI Solution Vector')
print(xNewGauss)
print('Tolerance met at: '+str(tol[-1])+'\n')

#! SOR method for solving by iterations
def SOR (A,b,x,w,i):
    n=len(x)
    xOld=copy(x)
    xNew=copy(x)
    # Reset each round
    Y =0.
    Z =0.
    c=w/A[i,i]
    frontC = (1-w)*xOld[i]
    X = b[i]
    for j in range(0,i):
        Y += A[i,j]*xNew[j-1]
    for j in range(i+1,n):
        Z += A[i,j]*xOld[j]
    xNew=(X-Y-Z)*c+frontC
    return xNew

# Consider this a test for SOR
tol = [1]
xNewSOR=copy(xk)
iteration=0
while tol[-1]>allowedTol:
    xOldSOR=copy(xNewSOR)
    iteration+=1
    for i in range(n):
        xNewSOR[i] = SOR(A,b,xOldSOR,w,i)
    tol.append(converge(xOldSOR,xNewSOR))
print('SOR iterations: '+str(iteration))
print('SOR Solution Vector')
print(xNewSOR)
print('Tolerance met at: '+str(tol[-1])+'\n')



# Problem 3 Use Relative Error

def relError (xOld, xNew):
    #out = np.linalg.norm(xNew-xOld, 1)/np.linalg.norm(xNew, 1)
    out = abs(xNew-xOld)/abs(xNew)
    return max(out)
	
errorGiven=[1E-6,1E-8]
for errStop in errorGiven:	
    print('************ '+str(errStop)+' ***********')
    # Consider this a test for Jacobi
    relErr = [1]
    # just to initialize
    xNewJac= copy(xk)
    iteration=0
    # Index last value in tolerance
    while relErr[-1]>errStop:
        xOldJac=copy(xNewJac)
        iteration+=1
        for i in range(n):
           xNewJac[i] = jacobi(A,b,xOldJac,i)
        relErr.append(relError(xOldJac,xNewJac))    
    print('Jacobi iterations: '+str(iteration))
    print('Jacobi Solution Vector')
    print(xNewJac)
    print('Tolerance met at: '+str(relErr[-1])+'\n')
    # Consider this a test for Gauss Siedel 
    relErr = [1]
    xNewGauss= copy(xk)
    iteration=0
    while relErr[-1]>errStop:
        iteration+=1
        xOldGauss=copy(xNewGauss)
        for i in range(n):
            xNewGauss[i] = GSI(A,b,xOldGauss,i)
        relErr.append(relError(xOldGauss,xNewGauss))
    print('GSI iterations: '+str(iteration))
    print('GSI Solution Vector')
    print(xNewGauss)
    print('Tolerance met at: '+str(relErr[-1])+'\n')
    
    relErr = [1]
    xNewSOR=copy(xk)
    iteration=0
    while relErr[-1]>errStop:
        xOldSOR=copy(xNewSOR)
        iteration+=1
        for i in range(n):
            xNewSOR[i] = SOR(A,b,xOldSOR,w,i)
        relErr.append(relError(xOldSOR,xNewSOR))
    print('SOR iterations: '+str(iteration))
    print('SOR Solution Vector')
    print(xNewSOR)
    print('Tolerance met at: '+str(relErr[-1])+'\n')


def relDiff (xOld,xNew):
    top = np.abs(xOld-xNew)
    bot = .5*(xOld+xNew)
    return top/bot

rangeEnd = 2
rangeStart = 0
differemce = 1E-6
relativeDiff = 1
prevBestW = -5
bestW=False
while relativeDiff>differemce:
    if bestW > -1:
        prevBestW=copy(bestW)
    iterationTaken =[]
    allWs = []
    possibleW = np.linspace(rangeStart,rangeEnd)
    for wopt in possibleW:
        tol = [1]
        xNewSOR=copy(xk)
        iteration = 0
        while tol[-1]>allowedTol:
            xOldSOR=copy(xNewSOR)
            iteration+=1
            for i in range(n):
                xNewSOR[i] = SOR(A,b,xOldSOR,wopt,i)
            tol.append(converge(xOldSOR,xNewSOR))
        iterationTaken.append(iteration)
        allWs.append(wopt)
    # ignore first value since its 1 or non optimal
    compareval = iterationTaken[1:]
    listOfW = allWs[1:]
    minIndex = compareval.index(min(compareval))
    # Should be same size as compare val
    bestW = listOfW[minIndex]
    rangeStart = allWs[minIndex-1]
    rangeEnd = allWs[minIndex+1]
    relativeDiff = relDiff(bestW,prevBestW)
print(bestW)
