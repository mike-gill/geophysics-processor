from DialogManager import *
from RawData import *
from ResistData import *
from MagnetData import *
from TextFileExporter import *
from XYZExporter import *
from GridPlotter import *

class GeophysConverter():
    """
    Main controlling class for converting a raw Resistivity
    or Magnetometer file.  The class is run by passing a file
    type argument ('R' for Resistivity or 'M' for
    Magenetometer file.

    Author:     M. Gill
    Copyright:  M. Gill
    """
    
    def __init__ (self):
        """
        Constructor
        """
        self.TYPE_RES = 'R'
        self.TYPE_MAG = 'M'

    def convertfile(self, filetype):
        """
        Main function which controls the processing of
        the raw data file

        filetype - the type of file to be converted -
                   (TYPE_RES or TYPE_MAG)
        """
        filename = self.locatefile()
        if filename == "":
            print "\nNo file was chosen, exiting ...\n"
            return
        else:
            print "\nRaw data file:\n" + filename
        
        print "\nReading raw data file...."
        rawdata = RawData(filename)
        print "FINISHED reading raw data file"
        
        print "\nExtracting readings from raw data ..."
        if filetype == self.TYPE_RES:     
            geodata = ResistData(rawdata)
        elif filetype == self.TYPE_MAG:
            geodata = MagnetData(rawdata)
        print "FINISHED extracting readings"

        outfname = (filename.replace('.', '_') +
                    '_REFORMATTED.txt')
        print "\nAbout to write formatted data ..."
        tfe = TextFileExporter()
        tfe.writefile(geodata, outfname)
        print "FINISHED writing data to:\n" + outfname

        outfname = (filename.replace('.', '_') +
                    '_XYZ.txt')
        print "\nAbout to write XYZ data ..."
        xyz = XYZExporter()
        xyz.writefile(geodata, outfname, 'x')
        print "FINISHED writing data to:\n" + outfname        

        print "\nAbout to render plot ..."
        gp = GridPlotter()
        title = "Plot of raw data file: " + filename
        outfname = (filename.replace('.', '_') +
                    '_PLOT.png')
        gp.plotgeodata(geodata, title, outfname)
        print "FINISHED rendering plot to:\n" + outfname
        print "\n\n"
        

    def locatefile(self):
        """
        Calls a class to open a file dialogue
        allowing the user to choose a text file.
        """
        dm = DialogManager()
        print "Opening file chooser ..."
        file = dm.choosefile("Choose Raw File")
        return file
    
def main(argv):
    gc = GeophysConverter()
    gc.convertfile(argv[0])
if __name__ == "__main__":
    main(sys.argv[1:])        


 