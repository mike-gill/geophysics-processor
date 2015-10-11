import matplotlib.pyplot as plt
from scipy import ndimage
import numpy

class Plot():
    def __init__(self, raster, title, cmap=plt.cm.gray):
        self.raster = raster
        self.title = title
        self.cmap = cmap

def plot_rasters(plotarr, filename_out, showAxis=False):
    axisflag = 'off'
    if showAxis:
        axisflag = 'on'
    
    numrows = len(plotarr)
    numcols = len(plotarr[0])
    fig, axarr = plt.subplots(nrows=numrows, ncols=numcols, figsize=(20, 20))

    for r in range(numrows):
        for c in range(numcols):
            ax = axarr[r, c]
            plot = plotarr[r][c]
            ax.imshow(plot.raster, cmap=plot.cmap)
            ax.set_title(plot.title)
            ax.axis(axisflag)
    #plt.show()
    plt.savefig(filename_out, bbox_inches='tight')
    

def gaussian(in_img, sigma):
    return ndimage.gaussian_filter(in_img, sigma)

def subtract(img1, img2):
    return img1 - img2

def createGaussianPlot(in_img, sigma):
    gauss_img = gaussian(in_img, sigma)
    diff_img = in_img - gauss_img
    return [Plot(gauss_img, "Gaussian Sigma %s" % (sigma)),
            Plot(in_img, "Original"),
            Plot(diff_img, "Diff Sigma %s" % (sigma)) ]

filename = r"EarthRes 26Sep15 11-31-24_cleaned_txt_REFORMATTED.txt"
filename_out = r"EarthRes 26Sep15 11-31-24_cleaned_txt_REFORMATTED Gaussian Subtract.pdf"
text_out = r"EarthRes 26Sep15 11-31-24_cleaned_txt_REFORMATTED Gaussian Subtract.txt"
in_img = numpy.rot90(numpy.loadtxt(filename, delimiter=",")).astype(numpy.int32)

plotarr = []
for sigma in [0.75, 1.0, 2.0, 3.0, 4.0, 7.0]:
    plotarr.append(createGaussianPlot(in_img, sigma))
plot_rasters(plotarr, filename_out)

# Write out diff image for sigma 7.0
numpy.savetxt(text_out, numpy.rot90(plotarr[5][2].raster + 100, 3), delimiter=',')


