import re
import numpy
from imports.lightCurve import lightCurve
from imports.plotter import *


def titleBreaker(name):
    return re.split("[_]", name)[2]


def main():
    #   Specifying the Data Directory and the Input File
    dirLocation = "../data/input/XSM Extracted Light Curve"
    inputFile = "ch2_xsm_20190912_v1_level2.lc"
    file = dirLocation + "/" + inputFile

    #   Specifying the binsize for rebinning, the minimum flare duration, bins used for boxed average
    #   Didn't take an input from the user because Sublime Text crashes on accepting inputs
    binsize = 12
    tMin = 60
    boxPts = 21

    #   Initializing an object for the class lightCurve
    #   And calling the respective functions. For more info,, read the comments in the lightCurve.py file
    lc = lightCurve(file, binsize, tMin, boxPts)
    lc.dataImport()

    #   Initializing an object for the class rawLightCurvePlotter in the file plotter.py

    rawPlot = rawLightCurvePlotter(lc.rawDataPoints()[0], lc.rawDataPoints()[
                                   1], str(titleBreaker(inputFile)))
    rawPlot.rawPlotter()

    #   Initialuzing an object for the class rebinnedLightCurvePlotter in the file plotter.py

    rebinnedPlot = rebinnedLightCurvePlotter(lc.reBinner()[0], lc.reBinner()[
                                             1], str(titleBreaker(inputFile)))
    rebinnedPlot.rebinPlotter()

    #   Initializing an object for the class smoothenedLightCurvePlotter in the file plotter.py

    smoothPlot = smoothenedLightCurvePlotter(
        lc.reBinner()[0], lc.smoother(), str(titleBreaker(inputFile)))

    smoothPlot.smoothPlotter()

    #   Initializing an object for the class smoothenedLightCurvePlotter in the file plotter.py
    minm = np.asarray(lc.minimaMaximaLocator()[0])
    maxm = np.asarray(lc.minimaMaximaLocator()[1])
    x = np.asarray(lc.reBinner()[0])
    y = np.asarray(lc.smoother())

    minMaxPlot = minimaMaximaPlotter(
        x, y, x[minm], y[minm], x[maxm], y[maxm], str(titleBreaker(inputFile)))

    minMaxPlot.minMaxPlotter()


if __name__ == "__main__":
    main()

else:
    print("RUN main.py")
