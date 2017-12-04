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
Xo = 0

# Probelem inferred values
D=3
bGiven=100.0
allowedTol = 1E-6

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

# Consider this a test that in a deployable would be either commented out or deleted
tol = [1]
xOld = copy(xk)
xNew= copy(xOld)
iteration=0
# Index last value in tolerance
while tol[-1]>allowedTol:
    xOld=copy(xNew)
    iteration+=1
    for i in range(len(A)):
       xNew[i] = jacobi(A,b,xOld,i)
    tol.append(converge(xOld,xNew))    
print('Jacobi iterations: '+str(iteration))
print(xNew)
print(tol)
	
def GSI (A,b,x):
    n=len(x)
    xOld=x
    xNew=np.zeros((n,1))
    for i in range(n):
        # Reset each round
        X =0
        Y =0
        Z =0
        c=1/A[i][i]
        X = b[i]
        if i==0:
            for j in range(1,n-1,1):
                Z += A[i][j]*xOld[j]
            xNew[i]=(X-Y-Z)*c
        elif i ==n-1:
            for j in range(n-2):
                Y += A[i][j]*xNew[j]
            xNew[i]=(X-Y-Z)*c
        else:
            for j in range(i-2):
                Y += A[i][j]*xNew[j]
            for j in range(i,n-1):
                Z += A[i][j]*xOld[j]
            xNew[i]=(X-Y-Z)*c
    return xNew

def SOR (A,b,x,w):
    n=len(x)
    xOld=x
    xNew=np.zeros((n,1))
    for i in range(n):
        # Reset each round
        X =0
        Y =0
        Z =0
        c=w/A[i][i]
        frontC = (1-w)*xOld[i]
        X = b[i]
        if i==0:
            for j in range(1,n-1,1):
                Z += A[i][j]*xOld[j]
            xNew[i]=(X-Y-Z)*c+frontC
        elif i ==n-1:
            for j in range(n-2):
                Y += A[i][j]*xNew[j]
            xNew[i]=(X-Y-Z)*c+frontC
        else:
            for j in range(i-2):
                Y += A[i][j]*xNew[j]
            for j in range(i,n-1):
                Z += A[i][j]*xOld[j]
            xNew[i]=(X-Y-Z)*c+frontC
    return xNew










# =============================================================================
# 
# tol = 1e9
# xOld = copy(xk)
# xNew=0
# iteration=0
# while tol>allowedTol:
#    xNew = GSI(A,b,xOld)
#    tol=converge(xOld,xNew)
#    xOld=xNew
#    iteration+=1
# print(xNew)
# print(tol)
# print('GSI iterations: '+str(iteration))
# 
# tol = 1e9
# xOld = copy(xk)
# xNew=0
# iteration=0
# while tol>allowedTol:
#    xNew = SOR(A,b,xOld)
#    tol=converge(xOld,xNew)
#    xOld=xNew
#    iteration+=1
# print(xNew)
# print(tol)
# print('SOR iterations: '+str(iteration))
# =============================================================================

# Problem 3 Use Relative Error

# =============================================================================
# def relErr (xOld, xNew):
# 	return np.abs(xOld-xNew)/np.abs(xOld)
# 	
# errorGiven=[1E-6,1E-8]	
# for errStop in errorGiven:
# 	tol=1E9
# 	xOld = copy(xk)
# 	xNew=0
# 	iteration=0
# 		tol=1E9
# 	xOld = copy(xk)
# 	xNew=0
# 	iteration=0
# 	while tol>errStop:
# 	   xNew = jacobi(A,b,xOld)
# 	   tol=relErr(xOld,xNew)
# 	   xOld=xNew
# 	   iteration+=1
# 	print(xNew)
# 	print(tol)
# 	print('Jacobi iterations: '+str(iteration))
# 		tol=1E9
# 	xOld = copy(xk)
# 	xNew=0
# 	iteration=0
# 	while tol>errStop:
# 	   xNew = GSI(A,b,xOld)
# 	   tol=relErr(xOld,xNew)
# 	   xOld=xNew
# 	   iteration+=1
# 	print(xNew)
# 	print(tol)
# 	print('GSI iterations: '+str(iteration))
# 	while tol>errStop:
# 	   xNew = SOR(A,b,xOld)
# 	   tol=relErr(xOld,xNew)
# 	   xOld=xNew
# 	   iteration+=1
# 	print(xNew)
# 	print(tol)
# 	print('SOR iterations: '+str(iteration))
# =============================================================================

