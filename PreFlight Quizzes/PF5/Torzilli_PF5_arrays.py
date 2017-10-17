# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 07:22:14 2017

@author: Robert
"""
import numpy as np
# Problem 1
#%%
# part b create an array with default values
a= np.ones((3,2))
b= np.zeros((3,2))
c = np.empty((3,2))
d = np.array([[1,1],[2,2],[3,3]])
e = np.full((3,2),7)
print(a)
print(b)
print(c)
print(d)
print(e)
#%%
# part c auto create an array with specific step
print(np.arange(0,14,2))
print(np.ogrid[0:14:2])
print(np.mgrid[0:14:2])
#%%
# part d reshape an array. Note that this has 8 values and is not evenly spaced
tmp1 = np.array([0,2,4,6,10,12,14,16])
print(np.reshape(tmp1,(4,2)))
#%%
# Problem 3
#part a  use tmp1 and slice it.
# Note since there are 8 values only teh 1st and 5th are sliced
tmp2 = tmp1[0:8:4]
print(tmp1)
print(tmp2)
#part b
tmp2[1]=0
print(tmp2)
#%%
# Problem 4
# =============================================================================
# Structured arrays Shows grade of homework as float, grade of PFQ as
# ints and title of project. Students are zero indexed
# =============================================================================
x = np.array([(30.5,88.5,30,34,6,"Unorginal"),(30.5,88.5,30,34,6,"Orginal"),
              (30.5,88.5,30,34,6,"Transport"),(30.5,88.5,30,34,6,"Test"),
              (30.5,88.5,30,34,6,"Spelling")], 
    np.dtype([('HW1', 'f8'),('HW2', 'f8'), ('PF1', int),
           ('PF2', int),('PF3', int), ('Project', 'S16')]))
print(x[3])
#%%
# Problem 5
# add given arrays
x = np.array([1,2])
y = np.array([3,4])
# =============================================================================
# Simple to the point easy to understand. Only works in one direction and can
# only be used on two arrays at the same time. Limted by shape
# =============================================================================
z = np.add(x,y)
print(z)
# =============================================================================
# Takes more of a setup in order to accomplish however it could do more since
# each array is treated as a row. It also allows operations to be used on any axis
# =============================================================================
xy = np.array([x,y])
z2 = xy.sum(axis =0)
print(z2)