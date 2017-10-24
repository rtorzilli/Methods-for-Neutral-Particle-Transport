# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:41:50 2017

@author: Robert
"""
import numpy as np
# Calculate absolute and relative error
# =============================================================================
#  xTS or xHat = numerical(true/exact)solution
#  xNS or xVector = real(computed approximate numerical) solution
# =============================================================================
# Given two solution vectors
# xTS
x0 = [.45,.95,.2,-.05,.6]
# xNS
x1 = [.5,.9,.3,-.1,.5]
# =============================================================================
#  Absolute Error = ||xHat - xVector||normLvL
#  Relative Error = ||xHat - xVector||normLvL/||xVector||normLvL
# =============================================================================

#x1 - x0
diffx0x1 = np.subtract(x1,x0)

# A]
# Using the 1st norm
x0_N1 = np.linalg.norm(x0,1)
x1_N1 = np.linalg.norm(x1,1)

#absErr = x1_N1 - x0_N1
absErr = np.linalg.norm(diffx0x1,1)
relErr = absErr/x0_N1
print("First Given Values")
print("Error Calculated with 1st Norm")
print("Absolute Error " + str(absErr))
print("Relative Error " + str(relErr))
# Finding 1st norm

# B]
# Using the 2nd norm
x0_N2 = np.linalg.norm(x0,2)
x1_N2 = np.linalg.norm(x1,2)

absErr = np.linalg.norm(diffx0x1,2)
relErr = absErr/x0_N2

print("\nError Calculated with 2nd Norm")
print("Absolute Error " + str(absErr))
print("Relative Error " + str(relErr))

# C]
# Using the infinity norm
x0_NInf = np.linalg.norm(x0,np.inf)
x1_NInf = np.linalg.norm(x1,np.inf)

absErr = np.linalg.norm(diffx0x1,np.inf)
relErr = absErr/x0_NInf

print("\nError Calculated with Inf Norm")
print("Absolute Error " + str(absErr))
print("Relative Error " + str(relErr))

# What is least restricitive (that is would cause the code to converge first?)

# =============================================================================
# In this case lets assume that all three norms converge as superlinear plots.
# If that is the case since we have no third iteration to get an accurate rate
# we can assume that the norm that is closest to 0 is the closest to converging
# which means it would have the fastest rate of convergence since it got to that 
# point the quickest.
# 
# In this case that would be the infinite norm.
# =============================================================================

# =============================================================================
#  Let x0 change and recalculate the convergance values
#  In this case we recalculate the abs and relative error
# =============================================================================
x0 = [.49,.92,.4,-.09,.51]
#x1 - x0
diffx0x1 = np.subtract(x1,x0)

# Using the 1st norm
x0_N1 = np.linalg.norm(x0,1)
x1_N1 = np.linalg.norm(x1,1)

#absErr = x1_N1 - x0_N1
absErr = np.linalg.norm(diffx0x1,1)
relErr = absErr/x0_N1
print("\n\nSecond Given Values")
print("Error Calculated with 1st Norm")
print("Absolute Error " + str(absErr))
print("Relative Error " + str(relErr))
# Finding 1st norm

# Using the 2nd norm
x0_N2 = np.linalg.norm(x0,2)
x1_N2 = np.linalg.norm(x1,2)

absErr = np.linalg.norm(diffx0x1,2)
relErr = absErr/x0_N2

print("\nError Calculated with 2nd Norm")
print("Absolute Error " + str(absErr))
print("Relative Error " + str(relErr))

# Using the infinity norm
x0_NInf = np.linalg.norm(x0,np.inf)
x1_NInf = np.linalg.norm(x1,np.inf)

absErr = np.linalg.norm(diffx0x1,np.inf)
relErr = absErr/x0_NInf

print("\nError Calculated with Inf Norm")
print("Absolute Error " + str(absErr))
print("Relative Error " + str(relErr))

# What do you observe? What does this mean about how you might select your 
# convergence criteria?

# =============================================================================
# We note that the Absolute and Relative errors for the 1st and 2nd norms change;
# the 1 st norm changes the most. Only the relative error for the infinite norm
# changes and it changes very slightly in comparison.
# 
# This means we might want to use the infinite norm as a baseline when we are 
# unsure how the data converges. It also means that the data changes the convergence
# rate enough that it would be worth while to sample the data and determine for
# each case which norm to use for the convergence in order to make more efficient
# rates.
# =============================================================================
