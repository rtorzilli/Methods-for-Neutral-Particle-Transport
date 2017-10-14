# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 17:37:39 2017

@author: Robert
"""
import numpy as np
from Torzilli_ElementClass import Element
class Isotope(Element):
    def __init__(self,neutronAmt,givenHalfLife,atomicNumberIso):
        Element.__init__(self,atomicNumberIso)
        self.T12 = givenHalfLife
        self.n = neutronAmt
    def decayCalculation(self):
        decayConstant = (np.log(2))/(self.T12)
        return decayConstant
    def printDecay(self):
        print("The Decay Constant is: " + str(self.decayCalculation()))