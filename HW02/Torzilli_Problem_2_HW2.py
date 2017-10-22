# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 11:37:28 2017

@author: Robert
"""
import matplotlib.pyplot as plt
# =============================================================================
# Plot Relative Error(relErr) as a function of 
# =============================================================================

# Given Data 
relErr=[8.44660179e-03,2.30286448e-03,9.84273963e-05,2.48043656e-05,9.98488163e-07]
Nc = [8,16,80,160,800]
h = [1.0,.5,.1,.05,.01]

# A] Meshspacing (h)
fig1 = plt.figure()
plotLog = fig1.add_subplot(111)
plotLog.loglog(h,relErr,'-ro')
plotLog.set_title("Relative Error vs MeshSpacing")
plotLog.legend(("RelativeError(MeshSpacing)"),loc = "upper left")
plotLog.set_xlabel("Mesh Spacing")
plotLog.set_ylabel("Relative Error")
plotLog.grid()
# B] Cell Count (Nc)
fig2 = plt.figure()
plotLog = fig2.add_subplot(111)
plotLog.loglog(Nc,relErr,'-bo')
plotLog.set_title("Relative Error vs Mesh Cells")
plotLog.legend(("RelativeError(Mesh Cells)"),loc = "upper right")
plotLog.set_xlabel("Number of Mesh Cells")
plotLog.set_ylabel("Relative Error")
plotLog.grid()

# What is the functional relationship between error and 
# mesh spacing / number of cells?
# =============================================================================
# We can see that as mesh spacing gets larger our error goes up and as the number
# of mesh cells increase the error goes down
# =============================================================================
