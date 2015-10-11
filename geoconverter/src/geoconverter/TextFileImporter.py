import csv
import numpy as np
from GenericData import *

class TextFileImporter():
    """
    Class to read an XYZ text file, such as one exported
    from Snuffle Geophysics software.

    Author:  Mike Gill
    Copyright:  Mike Gill
    """
    
    def __init__ (self, filename):
        """
        Constructor.
        filename - full path and file name of the ASCII
            text file.
        """        
        self.filename = filename
        self.genericdata = None
        self.__parse_file()
        

    def __parse_file(self):
        """
        Private method to read the raw text file into a
        two dimensional array
        """  
        arr = np.loadtxt(self.filename, delimiter=",")

        # Create data array object           
        self.genericdata = GenericData(arr)
