
'''If you remember, class comments utilise these types of marks. Here
you should put something about the class that describes it and its main purpose. For instance, the 
DataObject class is an object where data are held in and are instantiated from user input files'''

class DataObject:
   
    '''
    Method to instantiate object
    @param x: input x
    @param y: input y 
    '''
    def __init__(self,x,y):
        self.x=x;
        self.y=y;

    '''
    Method to get x
    @return: x
    '''
    @property
    def my_x(self):
        return self.x

    '''Method to set x
    @param x: input for x'''
    @my_x.setter
    def my_x(self, x):
        self.x = x
     
    '''Method that returns y
     @return: y''' 
    @property  
    def my_y(self):
        return self.y
    
    '''Method that sets y
    @param y: input for y'''
    @my_y.setter
    def my_y(self, y):
        self.y=y

    '''Method that adds x and y
    @return: adds x and y'''
    def add_data(self):
        return self.x+self.y