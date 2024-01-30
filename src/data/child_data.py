
from data.data_object import DataObject

'''
Created on May 31, 2016

Child class that holds data from input file.
@author: maltaweel
'''
class ChildData(DataObject):
    pass
    
    '''
    Constructor where the input are x, y, and z
    where the super constructor is called (i.e., from the parent)
    @param x: The x input
    @param y: The y input
    @param z: The z input
    '''
    def __init__(self, x,y,z):
        self.z=z
        DataObject.__init__(self,x, y)
    
    '''
    Set the z value
    '''  
    @property
    def my_z(self,z):
        self.z=z
     
    '''
     Return the z value
     @return: returns the z value
    '''  
    @my_z.setter
    def my_z(self):
        return self.z
   
    '''
     Calls parent method addData and adds z
     @return: a
    '''
    def addXYZ(self):
        self.a=self.add_data()+self.z
        return self.a