
class GenericData():
    """
    Generic data class used to store a 2D data array.

    TO DO - create an abstract class, GeoData for this, 
    the ResistData and MagnetData class.    

    Author:  Mike Gill
    Copyright:  Mike Gill
    """
    
    def __init__ (self, arrData):
        """
        Constructor.
        arrData - 2D data array. 
        """
        self.NULLVALUE = float('nan')
        self.data = arrData
         
                
            
        
