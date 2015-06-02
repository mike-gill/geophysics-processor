class XYZExporter():
    """
    Class to export formatted geophysics data
    to a csv file

    Author:  Mike Gill
    Copyright:  Mike Gill
    """
    
    def __init__ (self, sep=','):
        """
        Constructor.
        sep - optional argument defining the text
            separator to use.  Defaults to comma.
        """
        self.sep = sep

    def writefile(self, geodata, filename, nullvalue='nan'):
        """
        Writes the data to a text file.
        geodata - the data object
        filename - the file to write to
        nullvalue - optional argument defining the string
            to write for a null value
        """
        f = open(filename, 'w')
        val = ''
        data = geodata.data
        for r in range(0, len(data)):
            for c in range(0, len(data[r])):
                val = data[r][c]
                if val == geodata.NULLVALUE:
                    val = nullvalue
                # Rotate 90 degrees to left while exporting
                f.write(str(r) + self.sep + str(len(data[c]) - c - 1) + self.sep + str(val))
                f.write('\n')
        f.close()
        