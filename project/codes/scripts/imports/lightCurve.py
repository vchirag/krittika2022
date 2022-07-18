def main():
    print("RUN main.py")


if __name__ == "__main__":
    main()

else:
    from astropy.io import fits
    from scipy import stats
    import math
    import numpy as np

    #   Defining the primary working class of this pipeline

    class lightCurve():

        def __init__(self, lightCurve, binsize, tMin, boxPts):
            self.lightCurve = lightCurve
            self.binsize = binsize
            self.tMin = tMin
            self.boxPts = boxPts

    #   Employing the fitsopen module from astropy

        def dataImport(self):
            return fits.open(self.lightCurve)

    #   Returning the raw Data Points to check if the file has been inputted successfully
    #   Might remove this method later.

        def rawDataPoints(self):
            rawData = self.dataImport()[1].data
            return(rawData["TIME"], rawData["RATE"])

    #   Calculating the number of bins
        def binCalculator(self):
            return (math.floor(len(self.rawDataPoints()[0]) / self.binsize))

        def reBinner(self):
            #   Initial time resolution= 1 s
            #   Rebinned bins = 100

            bin_means, bin_edges, binnumber = stats.binned_statistic(
                self.rawDataPoints()[0], self.rawDataPoints()[1], statistic="median", bins=self.binCalculator())
            bin_width = (bin_edges[1] - bin_edges[0])
            bin_centers = bin_edges[1:] - bin_width / 2

            #   Relabeling x axis:

            temp = []

            for i in range(len(bin_centers)):
                temp.append(bin_centers[i] - bin_centers[0])

            bin_centers = temp

            return (bin_centers, bin_means)

        def smoother(self):
            box = np.ones(self.boxPts) / self.boxPts
            return (np.convolve(self.reBinner()[1], box, mode="same"))

        def minimaMaximaLocator(self):
            #   Local minima
            minm = (np.diff(np.sign(np.diff(self.smoother())))
                    > 0).nonzero()[0] + 1
            #   Local maxima
            maxm = (np.diff(np.sign(np.diff(self.smoother())))
                    < 0).nonzero()[0] + 1

            return(minm, maxm)
