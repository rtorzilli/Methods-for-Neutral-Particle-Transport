# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:53:47 2017

@author: Robert
"""
#Part C
import numpy as np

x=np.arange(0,4,.0001)
pi=np.pi

def err (x):
    return(((pi)**4)/384)*(np.sin(pi*x/2))*(x*(x-2)*(x-3)*(x-4))

emax = 0
index = 0
for i in x:
    e = err(i)
    if (e>emax):
        emax =e
        index = i
print("Maximum: "+str(emax)+" at: "+str(i))
print("From Wolfram Alpha Below")
print("Maximum: "+str(err(3.45321)) + ' at: 3.45321')