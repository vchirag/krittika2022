# KSP 3.0 - Stellar Flares
# An implementation of automated flare identification as in Markus J. Aschwanden and Samuel L. Freeland. Automated Solar Flare Statistics in
# Soft X-Rays over 37 Years of GOES Observations: The Invariance of Self-organized Criticality during Three Solar Cycles. ApJ, 754(2):112, August 2012. doi: 10.1088/
# 0004-637X/754/2/112.

# Group: Chirag Verma (IIT Roorkee), Gourav Kumawat (IISER Bhopal), Sarthak Talukdar (IISc Bangalore)
# Code merged and scripted by Chirag Verma (IIT Roorkee)


def main():

    from get_file import file_input
    from lightCurve import lightCurve
    from plotter import plotter
    from plotter import minMaxPlotter
    from plotter import bkgPlotter
    from plotter import noBkgPlotter
    from plotter import flarePlotter
    import numpy as np

    # A variable date to store the date of lightcurve
    date = file_input()[1]

    # Initialize a lightCurve class objec lc
    lc = lightCurve()

    # Store and plot raw X and Y datapoints
    # Flag = 0 implies a raw plot
    x, y = lc.rawDataPoints()
    plotter(x, y, date, 0)

    # Store rebinned X and Y datapoints
    # Flag = 1 implies a rebinned plot
    x, y = lc.rebinnedPoints()
    plotter(x, y, date, 1)

    # Store and plot smoothened X and Y datapoints
    # Flag = 2 implies a smoothened plot
    x = lc.rebinnedPoints()[0]
    y = lc.smoothenedPoints()
    plotter(x, y, date, 2)

    # Store and plot all minima and maxima in the given dataset
    # Flag = 3 implies a plot with all labelled minima and maxima
    minm, maxm = lc.allminMaxPoints()
    x = np.asarray(lc.rebinnedPoints()[0])
    y = np.asarray(lc.smoothenedPoints())
    minMaxPlotter(x, y, x[minm], y[minm], x[maxm], y[maxm], date, 3)

    # Store and plot specific minima and mxaima in the given dataset
    # Flag = 4 implies a plot with specific minima and maxima
    minm, maxm = lc.specificMinMaxPoints()
    x = np.asarray(lc.rebinnedPoints()[0])
    y = np.asarray(lc.smoothenedPoints())
    minMaxPlotter(x, y, x[minm], y[minm], x[maxm], y[maxm], date, 4)

    # Store and plot minima, maxima, and the corresponding constant background
    # Flag = 5 implies a plot with all specific minima and maxima with constant background
    # An approach by Gaurav and Sarthak

    bkg = lc.backgroundCalculator_approach1()[0]
    minm, maxm = lc.specificMinMaxPoints()
    x = np.asarray(lc.rebinnedPoints()[0])
    y = np.asarray(lc.smoothenedPoints())
    bkgPlotter(x, y, x[minm], y[minm],
               x[maxm], y[maxm], bkg, date, 5)

    # Store and plot minima, maxima, and the corresponding constant background
    # Flag = 6 imples a plot with all specific minima and maxima with constant background
    # An approach by Chirag
    # Stores mean, std in a single list
    mean, std = lc.backgroundCalculator_approach2()
    bkg = [mean, std]
    minm, maxm = lc.specificMinMaxPoints()
    x = np.asarray(lc.rebinnedPoints()[0])
    y = np.asarray(lc.smoothenedPoints())

    bkgPlotter(x, y, x[minm], y[minm], x[maxm], y[maxm], bkg, date, 6)

    # Plot data without points that lie below the background
    # Flag = 7 implies a plot without point below the background
    minm = lc.dataRemover()[0]
    maxm = lc.dataRemover()[1]
    y = np.asarray(lc.dataRemover()[2])
    x = np.asarray(lc.rebinnedPoints()[0])
    noBkgPlotter(x, y, x[minm], y[minm], x[maxm], y[maxm], date, 7)

    # Plot the identified flares
    tStart, tEnd = lc.flareFinder()
    y = np.asarray(lc.dataRemover()[2])
    x = np.asarray(lc.rebinnedPoints()[0])

    flarePlotter(len(tStart), x, y, tStart, tEnd, date)


if __name__ == "__main__":
    main()

else:
    print("RUN main.py")
