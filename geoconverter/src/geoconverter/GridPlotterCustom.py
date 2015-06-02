from pylab import *
import matplotlib as mpl
import numpy as np

class GridPlotterCustom:
    """
    Controls the production of a plot image from
    a geodata class.  The plot image contains
    a series of sub plots.

    Author:     M. Gill
    Copyright:  M. Gill
    """
    
    def __init__ (self):
        """
        Constructor
        """
        self.sdev = -9999
        self.mean = -9999
        self.min = -9999
        self.max = -9999
        self.shownulls = True


    def plotcsv(self, filename, delim, title, outfile):
        """
        Entry point to create a plot from a csv file.
        The CSV file should be a formatted file, not
        a raw data file.  Null values should be represented
        by nan (which indicates 'not a number').
        
        filename - a string of the full path and filename
            of the source data file
        delim    - the string delimiter in the file
        title    - the title for the plot
        outfile  - a string of the full path and filename
            of the out file
        """
        arr = np.loadtxt(filename,
                         delimiter=delim,
                         unpack=True)
        self.plotgrid(arr, title, outfile)
        

    def plotgeodata(self, geodata, title, outfile):
        """
        Entry point to create a plot from a geodata object.
        
        geodata  - the geodata object to be plotted
        title    - the title for the plot
        outfile  - a string of the full path and filename
            of the out file
        """
        
        # Array columns and rows need to be swapped in order
        # to be shown properly on the plot (np.transpose())
        self.plotgrid(np.transpose(np.array(geodata.data)),
                      title,
                      outfile)


    def plotgrid(self, arr, title, outfile):
        """
        The main controlling method for the production
        of a plot file.
        
        arr     - the geodata object to be plotted
        title   - the title for the plot
        outfile - a string of the full path and filename
            of the out file
        """
        # Calculate relevant stats
        self.calcstats(arr)        

        # Find positions of nulls
        arrnulls = self.getnullindexes(arr)

        # Clear figure and set global figure settings        
        plt.clf()
        mpl.rc('xtick', labelsize=8)
        mpl.rc('ytick', labelsize=8)
        mpl.rc('savefig', dpi=300)

        #fig = plt.figure(figsize=(30,10))
        fig = plt.figure(figsize=(10,10))
        plt.title(title)

        # Calculate lower and upper limit values for
        # the 2 standard deviations plot
        sdev_lower = self.mean - 2*self.sdev
        if sdev_lower < self.min:
            sdev_lower = self.min
        sdev_upper = self.mean + 2*self.sdev
        if sdev_upper > self.max:
            sdev_upper = self.max

        # Create the subplots
        self.makeplot(arr, 331, 'nearest', cm.gray, [],
                 'Grey nearest', 10,
                 True, True, arrnulls)
        self.makeplot(arr, 332, 'bilinear', cm.gray, [],
                 'Grey bilinear', 10,
                 True, True, arrnulls)
        self.makeplot(arr, 333, 'nearest', cm.gray,
                 [sdev_lower, sdev_upper],
                 'Two STDEV nearest ', 10,
                 True, True, arrnulls)
        self.makeplot(arr, 334, 'nearest', cm.jet, [],
                 'Colour nearest', 10,
                 True, True, arrnulls)
        self.makeplot(arr, 335, 'bilinear', cm.jet, [],
                 'Colour bilinear', 10,
                 True, True, arrnulls)
        self.makeplot(arr, 336, 'bilinear', cm.gray,
                 [sdev_lower, sdev_upper],
                 'Two STDEV bilinear', 10,
                 True, True, arrnulls)
        self.makeplot(arr, 337, 'nearest', cm.jet,
                 [sdev_lower, sdev_upper],
                 'Two STDEV nearest', 10,
                 True, True, arrnulls)
        self.makeplot(arr, 338, 'bilinear', cm.jet,
                 [sdev_lower, sdev_upper],
                 'Two STDEV bilinear', 10,
                 True, True, arrnulls)

        # Save the figure to file        
        plt.savefig(outfile)

        
    def makeplot(self,
                 arr,
                 plotref,
                 interp,
                 colmap,
                 col_lim,
                 title,
                 titlesize,
                 showlegend,
                 showgrid,
                 arrnulls):
        """
        Controls the creation of a subplot.
        
        arr     - the 2D array to be plotted
        plotref - the subplot position index
        interp  - the interpolation method (eg bilinear)
        colmap  - the colormap (eg cm.jet)
        col_lim - lower and upper data limits as an array
            of format [lower_val, upper_val]
        title   - the title to be shown for the subplot
        titlesize - the font size
        showlegend - boolean controlling legend display
        showgrid - boolean controlling grid display
        arrnulls - 2D array of null value indexes in form
            [[r,c],[r,c]]
        """
        ax = plt.subplot(plotref)
        imgplot = plt.imshow(arr, origin='lower',
                             interpolation=interp, cmap=colmap)
        if len(col_lim) != 0:
            imgplot.set_clim(col_lim[0], col_lim[1])
        plt.grid(showgrid)
        if showlegend:
            plt.colorbar()
        plt.title(title, size=titlesize)
        if len(arrnulls) > 0:
            self.plotnulls(ax, arrnulls)
            

    def getnullindexes(self, arr):
        """
        Calculates the row and column indexes for null
        values.

        arr - the 2D array
        returns - 2D array of null value indexes in form
            [[r,c],[r,c]]
        """
        arrnulls = []
        for r in range(0, len(arr)):
            for c in range(0, len(arr[r])):
                if math.isnan(arr[r][c]):
                    arrnulls.append([r, c])
        return arrnulls


    def plotnulls(self, ax, arrnulls):
        """
        Displays a small red cross at the position
        of a null value on the plot

        ax - the plot axes
        arrnulls - 2D array of null value indexes in form
            [[r,c],[r,c]] 
        """
        if self.shownulls:
            ax.set_autoscale_on(False)
            if len(arrnulls) == 0:
                return

            for i in range(0, len(arrnulls)):
                ax.plot([arrnulls[i][1]], [arrnulls[i][0]],
                        'rx', markersize=3, mew=1)
            

    def filternans(self, arr):
        """
        Creates a list of values from a 2D array, filtering
        out nan (not a number) values.

        arr - the array of values to be filtered
        returns - a filtered list of values 
        """
        list = []
        for r in range(0, len(arr)):
            for c in range(0, len(arr[r])):
                if not math.isnan(arr[r][c]):
                    list.append(arr[r][c])
        return np.array(list)
    

    def calcstats(self, arr):
        """
        Calculates mean and standard deviation
        statistics for an array of values.

        arr - the array for which stats are to be
            calculated 
        """
        arrfilt = self.filternans(arr)
        self.sdev = np.std(arrfilt)
        self.mean = np.mean(arrfilt)
        self.min = np.min(arrfilt)
        self.max = np.max(arrfilt)

