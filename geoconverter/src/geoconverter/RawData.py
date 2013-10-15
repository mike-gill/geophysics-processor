import csv

class RawData():
    """
    Class to read a raw Geophysics raw data file and
    store the 2D data array as the data property of
    the class

    Author:  Mike Gill
    Copyright:  Mike Gill
    """
    
    def __init__ (self, filename):
        """
        Constructor.
        filename - full path and file name of the ASCII
            text file from the data logger.  Note this
            should not be the 'OrigData' file, rather its
            associated file.
        """        
        self.filename = filename
        self.data = []
        self.__parse_file()
        

    def __parse_file(self):
        """
        Private method to read the raw text file into a
        two dimensional array
        """        
        reader = csv.reader(open(self.filename), delimiter=',')
        self.data = []
        
        for row in reader:
            arr = []
            for i, s in enumerate(row):
                # Strip spaces from either end of string
                v = s.strip()
                if v.find("Row") != -1:
                    # Last column has value appended with ' Row n'
                    arr.append(float((v.split('Row')[0]).strip()))
                    if (len(arr) > 0):
                        self.data.append(arr)
                    break

                if v.find("Col") != -1:
                    break

                arr.append(float(v))
