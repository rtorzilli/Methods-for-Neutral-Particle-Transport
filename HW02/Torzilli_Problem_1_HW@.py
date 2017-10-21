# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:41:50 2017

@author: Robert
"""
import numpy as np
# Given two solution vectors
# 
x0 = [.45,.95,.2,-.05,.6]
x1 = [.5,.9,.3,-.1,.5]

# Calculate absolute and relative error
# =============================================================================
#  xTS = numerical(true/exact)solution
#  xNS = real(computed approximate numerical) solution
# =============================================================================

# =============================================================================
#  Absolute Error = ||xHat - xVector||normLvL
#  Relative Error = ||xHat - xVector||normLvL/||xVector||normLvL
# =============================================================================



# A]
# Using the 1st norm
x0_N1 = np.linalg.norm(x0,1)
x1_N1 = np.linalg.norm(x1,1)

#x0 - x1
diffx0x1 = np.subtract(x0,x1)

#absErr = x1_N1 - x0_N1
absErr = np.linalg.norm(diffx0x1,1)
relErr = absErr/x0_N1

print("Error Calculated with 1st Norm")
print("Absolute Error " + str(absErr))
print("Relative Error " + str(relErr))
# Finding 1st norm

# B]
# Using the 2nd norm
x0_N2 = np.linalg.norm(x0,2)
x1_N2 = np.linalg.norm(x1,2)

absErr = x1_N2 - x0_N2
relErr = absErr/x0_N2

print("\nError Calculated with 2nd Norm")
print("Absolute Error " + str(absErr))
print("Relative Error " + str(relErr))

# C]
# Using the infinity norm
x0_NInf = np.linalg.norm(x0,np.inf)
x1_NInf = np.linalg.norm(x1,np.inf)

absErr = x1_NInf - x0_NInf
relErr = absErr/x0_NInf

print("\nError Calculated with Inf Norm")
print("Absolute Error " + str(absErr))
print("Relative Error " + str(relErr))
