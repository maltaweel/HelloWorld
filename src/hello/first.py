'''
Created on May 24, 2016

@author: maltaweel
'''
 
'''This is a class called First
Classes are ways to create object-oriented code. We will talk about object-oriented 
programming next week.'''



class First:   
    
    
    '''This is a method, here defined as def, which is a generic form for methods.
     The method (init()) initializes the object when it is created, taking two
     input variables, called realpart and imagpart. What happens then is they are
     assigned to the object variables r and i, where self is the object of reference.
    
     @param realpart: a name of an input variable
     @param imagpart: a name of another input variable'''
    
    def __init__(self, realpart, imagpart): 
        
        #here realpart is set to the object variable r
        self.r = realpart  
        
        #here imagpart is set to the object variable i
        self.i = imagpart  

    '''Now this method simply calculates based on conditionals. 
     Notice self is in the method but it will not be utilized in calling the method
     from outside the class.
     @return: r*5'''
       
    def calculate(self):
        
    #If less than 5, it should be 5
        if(self.r<5):
            self.r=5
            
    #otherwise it is just 1
        else:
            self.r=1
        #return r * 5
        return self.r*5


    '''
      This method, called employ, initializes a variable i and then uses a while loop
      Nothing fancy here, just printing i and iterating by increasing by 1 the value
      of i.
     '''
    def employ(self):
        #simply iterates such that 1 is added to i
        i=0
        while i < self.i:
            print(i)
            i+=1
            
    '''
     Now we do an exercise using the for loop.
     Array a is iterated over, if the array value is less than 7 then print the value
     ''' 
    def forLoop(self):
        a=[2,4,6,8,10,12,14]
        for i in a:
            if(i<7): print(a[i]) 
            
            
            

#To run the program, let's first create the object called c      
f=First(3.0,4.0)

#Let's now call a method in the object, the calculate method. Notice self
#does not need calling.
print(f.calculate())

#Run employ
f.employ()

#Run forLoop
f.forLoop()
    