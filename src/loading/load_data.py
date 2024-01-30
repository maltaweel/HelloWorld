import csv
import os

from data.child_data import ChildData
from analysis.data_analysis import DataAnalysis

'''
Created on August 1, 2023

This is a class where data are loaded from a .csv file.
That file's data are then passed to the data object.
The data object is then used for analysis.

@author: maltaweel
'''



def run():

    #This is code executed outside the class but will call this and other classes

    #This code changes the current directory so relative paths are used
    pn=os.path.abspath(__file__)
    pn=pn.split("src")[0]
        

    #The data file path is now created where the data folder and dataFile.csv is referenced
    path=os.path.join(pn,'data','dataFile.csv')

    #The data are now loaded
    ld=LoadData(path)

    #This loads data into your data object
    ld.runFile()

    #Now we do a simple addition calculation
    ld.cd.addXYZ()

    #Now we create an analysis object
    an=DataAnalysis(ld.cd)

    #Here we do three different analyses with the input
    #first a quadratic calculation
    print('Quadratic:', an.doQuadratic())

    #then a Fibonacci calculation
    print('Fibonacci:',an.doFibonacci(ld.cd.a))

    #then we return the hypotenuse using the pythagorean theorem
    print('Hypotenuse',an.hypotenuse_pythagorean())

    ##print(ld.cd.x+" : "+ld.cd.y+" : "+ld.cd.z)
    #print(ld.cd.a)
    
class LoadData:
    
    '''
    This instantiates the class with a reference to a file location (i.e., where a file is)
    @param fileLocation: The location of the file (i.e., its path''' 
    def __init__(self,fileLocation):
        self.fileLocation=fileLocation
    
    '''
    This opens the file and puts the data in the appropriate places in the data file
    '''
    def runFile(self):
        
        #first, open the file and put into object f, open is a built-in method to open a file
        with open(self.fileLocation, 'r') as csvfile:
        
        #We can use a try clause to read the file
       
            reader = csv.DictReader(csvfile)
            
            #for loop, skipping the first line (i.e., when i is 0), since this is the title line
            for row in reader:
                
                #starting in line 2 we get the data, x, y, and z
                #Then create the ChildData object and put the data there
                x=float(row['x'])
                y=float(row['y'])
                z=float(row['z'])
                self.cd=ChildData(x,y,z)
               
      
            csvfile.close()


if __name__ == '__main__':
    run()
    

