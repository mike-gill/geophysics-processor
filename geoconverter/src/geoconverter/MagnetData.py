import numpy as np

class MagnetData():
    """
    Class to read a raw Magnetometer data array and
    store the cleaned 2D data array as the data
    property of the class

    TO DO - create an abstract class, GeoData for this
    and the ResistData class.

    Author:  Mike Gill
    Copyright:  Mike Gill
    """
    
    def __init__ (self, rawdata):
        """
        Constructor.
        rawdata - RawData object containing 2D data
            array. 
        """
        self.NULLVALUE = float('nan')
        self.all_readings = []
        self.__extractdata(rawdata.data)


    def __extractdata(self, arrraw):
        """
        Extracts the actual readings from the raw data
        array
        
        arrraw - the raw data array
        """
        self.all_readings = []

        # Flatten array in column order
        arr_flat = np.ravel(np.array(arrraw), order='F')

        # Calculate end index of each block of
        # 12 values equal to 24929
        arrheaders = self.findheaders(arr_flat)

        # Filter out data values
        # First set is a special case, as only one block
        # of 24929's
        self.all_readings.append(self.readdatablock(arr_flat,
                                   arrheaders[0] + 2,
                                   arrheaders[1] - 14))

        # Step by 2
        for i in range(2, len(arrheaders) - 2, 2):
            self.all_readings.append(self.readdatablock(arr_flat,
                arrheaders[i] + 2,
                arrheaders[i + 1] - 14))

        # Calculate difference values for the readings
        # and store in data property
        self.calcdiffvalues()

        # Fill in any missing values with NaN
        self.fillnulls(self.data)            
        

    def findheaders(self, arr_flat):
        """
        Finds the end index of each set of 12 values
        equal to 24929
        
        arr_flat - the flattened data array
        returns - an array of indexes
        """
        
        arrheaders = []

        n24929count = 0
        for i in range(0, len(arr_flat)):
            if arr_flat[i] == 24929:
                n24929count = n24929count + 1
            else:
                if n24929count == 12:
                    arrheaders.append(i - 1)
                n24929count = 0

        return arrheaders
    

    def readdatablock(self, arr_flat, istart, iend):
        """
        Reads the block of data between two indexes
        
        arr_flat - the flattened data array
        istart - the start index
        iend - the end index
        returns - an array of data values
        """
        
        arr = []
        for i in range(istart, iend + 1):
            arr.append(arr_flat[i])
        return arr
    

    def calcdiffvalues(self):
        """
        Calculates the difference between each set of
        two readings in the all_readings data array,
        and appends to the array stored in the data
        property.
        """
        
        self.data = []
        for r in range(0, len(self.all_readings)):
            arr = []
            for c in range(0, len(self.all_readings[r]) - 1, 2):
                diffval = (self.all_readings[r][c] -
                           self.all_readings[r][c+1])
                arr.append(diffval)
            self.data.append(arr)
                


    def fillnulls(self, arr):
        """
        Appends null values to the end of any
        short rows in the data array.

        arr - the array to which nulls will be
            appended.
        """
                            
        # Find max length of row
        maxlen = 0
        for n in range(0, len(arr)):
            if len(arr[n]) > maxlen:
                maxlen = len(arr[n])
        # Fill in null values
        for n in range(0, len(arr)):
            if len(arr[n]) < maxlen:
                for i in range(len(arr[n]), maxlen):
                    arr[n].append(self.NULLVALUE)
                        
                
            
        
