# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:04:05 2017

@author: Robert
"""
import numpy as np
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
A_matrix_sta = np.array([[0,2,-1]])
# Create a mold to repeat
A_matrix_mid_val = np.array([[-1,2,-1]]) 
A_matrix_mid = np.repeat(A_matrix_mid_val,n-2, axis = 0)
A_matrix_end = np.array([[0,2,-1]])
# Combine begining middle and end parts
A_matrix_tmp = np.concatenate([A_matrix_sta,A_matrix_mid])
A_matrix = np.concatenate([A_matrix_tmp,A_matrix_end])
print(len(A_matrix))
print(len(bVector))
inverseA = np.invert(A_matrix)
print(inverseA)
print(inverseA*A_matrix)

# B]
# What is the condition number of A?
