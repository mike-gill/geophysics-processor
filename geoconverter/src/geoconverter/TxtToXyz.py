import sys
from XYZExporter import *
from TextFileImporter import *

class TxtToXyz():
    """
    Class to export an xyz file
    to a csv file

    Author:  Mike Gill
    Copyright:  Mike Gill
    """
    
    def __init__ (self):
        """
        Constructor.
        """
        pass

    def convert_file(self, in_filename, out_filename, nullvalue='nan'):
        """
        Writes the data to a text file.
        geodata - the data object
        filename - the file to write to
        nullvalue - optional argument defining the string
            to write for a null value
        """
        importer = TextFileImporter(in_filename)
        geodata = importer.genericdata

        exporter = XYZExporter()
        exporter.writefile(geodata, out_filename)
		
def main(argv):
    converter = TxtToXyz()
    converter.convert_file(argv[0], argv[1])
if __name__ == "__main__":
    main(sys.argv[1:])               