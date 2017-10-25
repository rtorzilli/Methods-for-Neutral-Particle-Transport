# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:04:05 2017

@author: Robert
"""
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt
# A]  Construct A and bVector
n = 100
# Making bVector
bVector_start = [0]
bVector_mid = np.arange(1,n-1)
bVector_end = [n-1]
# Combine begining middle and end parts
bVector_tmp = np.concatenate([bVector_start,bVector_mid])
bVector = np.concatenate([bVector_tmp, bVector_end])

# Make A matrix
# Create a mold to repeat
A_matrix = np.zeros((n,n))
A_matrix[0,0]=2
A_matrix[0,1]=-1
# Row Track, don't want to overwrite zeros
j = 0
#Column track
for i in range(1,n-1):
    if (j<=97):
        j += 1
        A_matrix[i,j-1]=-1
        A_matrix[i,j]=2
        A_matrix[i,j+1]=-1
A_matrix[n-1,n-2]=-1
A_matrix[n-1,n-1]=2
# B]
# What is the condition number of A?
# Since no norm value was specified I am leaving it at the default 2-norm
conditionA = np.linalg.cond(A_matrix)
print("Condition Number of A: " + str(conditionA))

# C]
# Explicitly solve the X values using inverse multiplication
inverseA = np.linalg.inv(A_matrix)
identityProof = (np.matmul(inverseA,A_matrix))
solutionExplicit = np.matmul(inverseA,bVector)

# D]
# Solve the X values using scipy's solve function
solutionScipy = solve(A_matrix,bVector)

# Plot the "explicit" and scipy's numerical solutions on the same plot
plt.title("Found Solutions to the Linear Equation in Prb 5")
plt.plot(solutionExplicit,bVector,'-ro')
plt.plot(solutionScipy,bVector,'-b*')
plt.legend(("Explicit","Scipy"),loc = "center left")
plt.xlabel("Soultion Values (X)")
plt.ylabel("Given bVector (Y)")