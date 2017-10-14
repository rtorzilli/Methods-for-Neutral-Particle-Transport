# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 18:39:56 2017

@author: Robert
"""
from Torzilli_ElementClass import Element
from Torzilli_IsotopeClass import Isotope

densityU = 19.1     
numberU = 92
massU = 238.03 
myElement = Element(numberU, densityU)

# Print the state of the object
print("Problem 2")
myElement.printState()
print()

#Run it, run printState to prove inheritance
myHalfLife = 3
totalNeutrons = 50
numberUr = 100
myIsotope = Isotope(totalNeutrons,myHalfLife,numberUr)
print("Problem 4")
myIsotope.printDecay()
myIsotope.printState()