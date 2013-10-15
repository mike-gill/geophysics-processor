import csv
import numpy as np
from GenericData import *

class XYZImporter():
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
        reader = csv.reader(open(self.filename), delimiter=' ')
        self.data = []

        maxx = 0
        maxy = 0
        # Find array dimensions
        for row in reader:
            maxx = max(maxx, int(row[0]))
            maxy = max(maxy, int(row[1]))

        # Initialize array
        self.data = [[0 for col in range(maxy + 1)] for row in range(maxx + 1)]

        reader = csv.reader(open(self.filename), delimiter=' ')
        
        for row in reader:
            c = int(row[0])
            r = int(row[1])
            v = float(row[2])
            # Rotate values through 90 degrees when setting array values
            self.data[c][maxy - r] = v

        # Create data array object           
        self.genericdata = GenericData(self.data)
