'''
Created on Oct 9, 2017

@author: Robert
'''
#===============================================================================
# (5 points) Define a function that returns the product (i.e. ) of an unknown set of
# numbers.
#===============================================================================

def mathProduct(xi):
    total = 1
    for i in xi:
        total = total*i
    return total

answer=mathProduct([3,2,5])
print(answer)

