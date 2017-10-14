# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 17:01:25 2017

@author: Robert
"""
# =============================================================================
# Describe an element. Give it attributes (args) of density (N), 
# atomic number (Z), atomic mass (A)
# =============================================================================
class Element():
    # The Constructor. It should require the Atoimc Number
    def __init__(element,atomicNumber,atomicDensity = -5,atomicMass = -5):
        element.N = atomicDensity
        element.Z = atomicNumber
        element.A = atomicMass
    #Create a method to print out the state of the object
    def printState(self):
        print("Atomic Number: " + str(self.Z))
        if (self.N != -5):
            print("Atomic Density: " + str(self.N))
        if (self.A != -5):
            print("Atomic Mass: " + str(self.A))