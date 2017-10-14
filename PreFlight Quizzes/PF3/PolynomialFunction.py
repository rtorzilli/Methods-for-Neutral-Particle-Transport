'''
Created on Oct 9, 2017

@author: Robert
'''
#===============================================================================
# (10 points) Define a function that returns the value of up to a 4-dimensional polynomial
# for a given input and set of parameters for the polynomial. Only the linear terms must
# be specified, the other terms are optional.
#===============================================================================

def genericPoly(*dims):
    outDim = "No value inserted"
    if (len(dims) > 0): 
        dim1 = dims[0]**3
        outDim = [dim1]        
    if (len(dims) >1): 
        dim2 = dims[0]**3+dims[1]**2
        outDim=[dim1,dim2]
    if (len(dims) >2): 
        dim3 = dims[0]**3+dims[1]**2+dims[2]
        outDim.append(dim3)
    if (len(dims) >3):
        dim4 = (dims[0]**3+dims[1]**2+dims[2])/dims[3]
        outDim.append(dim4)
    if (len(dims) >4):
        print("Only the first 4 terms will be used")
    return outDim

def genericPolynomial(x,y=0,z=0,t=1):
    if (t==0):
        t=1
        print("t can not equal zero")
    return (x**3+y**2+z)/t

allDim=genericPoly(5,3,4,1)
print(allDim)
allDim=genericPolynomial(2,t=0)
print(allDim)