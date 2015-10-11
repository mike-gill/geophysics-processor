from DialogManager import *
from RawData import *
from ResistData import *
from MagnetData import *
from TextFileExporter import *
from XYZExporter import *
from XYZImporter import *
from GridPlotterCustom import *

class SnufflerXYZPlotter():
    """
    Main controlling class for plotting a Snuffler
    XYZ file

    Author:     M. Gill
    Copyright:  M. Gill
    """
    
    def __init__ (self):
        """
        Constructor
        """


    def plotfile(self):
        """
        Main function which controls the plotting of
        the XYZ data file
        """
        filename = self.locatefile()
        if filename == "":
            print "\nNo file was chosen, exiting ...\n"
            return
        else:
            print "\nXYZ Data file:\n" + filename
        
        print "\nReading XYZ data file...."
        xyz = XYZImporter(filename)
        geodata = xyz.genericdata
        print "FINISHED reading XYZ data file"

        # Note PNG is only 8 bit, and so PDF has greater colour
        # depth        
        print "\nAbout to render plot ..."
        gp = GridPlotterCustom()
        gp.shownulls = False
        title = "Plot of XYZ data file: " + filename
        outfname = (filename.replace('.', '_') +
                    '_PLOT_custom.pdf')
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
    sp = SnufflerXYZPlotter()
    sp.plotfile()
if __name__ == "__main__":
    main(sys.argv[1:])        


 