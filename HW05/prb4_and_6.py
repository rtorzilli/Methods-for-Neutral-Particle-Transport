# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:19:59 2017

@author: Robert
"""
import matplotlib.pyplot as plt
import numpy as np

# Given values
# Boundary condition
a=4.0
# first source term assuming its the same for everything
S0 = 8.0
# Assumption homogeneneous, uniform mesh thus h, D, and macroAbs are constant
h=.1
D=1.0
macroAbs=.2

# Problem calls for the use of the finite diff and Gaussian elimination
# Use finite diff to create matrix A and Gaussian elimination to solve 
# Ax=b

# Finite difference for a homogenerous uniform mesh which I am assuming
def finiteDiff():
    # first row
    if i == 0:
        a[i,i] = 2*D/(h**2)+sigma
        a[i,i+1] = -2*D
        #built in python funciton
        diags([value],[i-1,i,i+1])
    if i == n-1:
        kjh
    else:
        

    
    
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
    
    
# plot results for Phi(x)vs x
# =============================================================================
# 
# xAxis = copy(x)
# yAxis = copy (phi)
# # Plotting:
# figureFile = plt.figure()
# plt.rcParams.update({'font.size': 10})
# plt.errorbar(xAxis, # X-Axis
#              yAxis, # Y-Axis
#              label='Calculted',
#              color='k',
#              # Markers:
#              marker='^',
#              markersize=10,
#              markeredgecolor='r',
#              # Error Bars:
#              capsize=10, # error bar capsize
#              capthick=1,
#              ecolor='r')
# #
# # =============================================================================
# # plt.errorbar(xAxis, # X-Axis
# #              amtOfVals*effMCNP, # Y-Axis
# #              yerr=amtOfVals*effMCNP*uncertMCNP,  # Error Bars
# #              label='MCNP',
# #              color='g',
# #              # Markers:
# #              marker='o',
# #              markersize=10,
# #              markeredgecolor='m',
# #              # Error Bars:
# #              capsize=5, # error bar capsize
# #              capthick=1,
# #              ecolor='m')
# # =============================================================================
# #
# plt.legend(loc='upper right',prop={'size': 8})
# plt.xlabel('x')
# plt.ylabel('phi(x')
# plt.title('Ax=b solution using numerical analysis')
# =============================================================================
