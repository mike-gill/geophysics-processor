
class ResistData():
    """
    Class to read a raw Geophysics raw data file and
    store the 2D data array as the data property of
    the class

    TO DO - create an abstract class, GeoData for this
    and the MagnetData class.    

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
        self.data = []
        self.__extractdata(rawdata.data)
        

    def __extractdata(self, arrraw):
        """
        Extracts the actual readings from the raw data
        array
        
        arrraw - the raw data array
        """
        self.data = []

        globalstartindex = -1        

        for r in range(0, len(arrraw)):
            startindex = -1
            arr = []
                       
            for c in range(0, len(arrraw[r])):
                val = arrraw[r][c]
                if val == 0:
                    if startindex != -1:
                        if (len(arr) > 0):
                            self.data.append(arr)
                        break
                else:
                    arr.append(val - 32256)
                    if startindex == -1:
                        startindex = c
                        if globalstartindex == -1:
                            globalstartindex = startindex
                        else:
                            # Ensure start index is the same for
                            # all rows
                            if startindex != globalstartindex:
                                raise Exception(
                                    "Start Index mismatch")

        # Fill in any missing values with NaN
        self.fillnulls(self.data)
        

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
                        
                
            
        
