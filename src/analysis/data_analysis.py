import math
import cmath
'''
Created on August 1, 2023

@author: maltaweel

This is a class to do some basic analysis on the data object. This analysis includes 
three methods, doing a quadratic equation, fibonacci number, and a pythagorean calculation
'''

class DataAnalysis():
    pass

    '''The constructor
    @param ChilData:  The object child data which contains the x, y, and z data
    '''
    def __init__(self, ChildData):
        self.childData=ChildData
        
    '''
    Do some a quadratic calculation
    '''
    def doQuadratic(self):
        
        #get the x, y, and z variables and convert to a, b, and c
        #here we convert to floats
        a = float(self.childData.x)
        b = float(self.childData.y)
        c = float(self.childData.z)
        
        
        # calculating  the discriminant
        dis = (b**2) - (4 * a*c)
 
        # find two results
        x1 = (-b-cmath.sqrt(dis))/(2 * a)
        x2 = (-b + cmath.sqrt(dis))/(2 * a)
 
    
        #return results
        return x1, x2
    '''
    Method for calculating the next number in a Fibonacci csequence.
    @param n: the current value in a Fibonacci sequence 
    '''
    def doFibonacci(self,n):
        if n == 0: return 0
        elif n == 1: return 1
        else: return self.doFibonacci(n-1)+self.doFibonacci(n-2)
    
    '''
    Method for calculating the hypotenuse
    Here we assume x and y are two sides of a triangle and so we calculate 
    what that hypotenuse should be.''
    '''    
    def hypotenuse_pythagorean(self):
        return math.sqrt(math.pow(self.childData.x,2)+math.pow(self.childData.y,2))
       
        
    