def main():
    print("RUN main.py")


if __name__ == "__main__":
    main()

else:

    from astropy.io import fits
    from astropy.convolution import convolve, Box1DKernel
    from scipy import stats
    import math
    import numpy as np
    from scipy.signal import argrelmin
    from scipy.signal import argrelmax
    import pandas as pd

    # Import the file->dataframe converter from get_file.py
    from get_file import dataFrameReturner

    # Store the dtaframe in a variable named "df"
    df = dataFrameReturner()

    class lightCurve():

        # Colelct raw data points

        def rawDataPoints(self):
            rawX = df["TIME"]
            rawY = df["RATE"]

            return (rawX, rawY)

        # Rebin the previously attained data
        def rebinnedPoints(self):

            x, y = self.rawDataPoints()
            binsize = 50
            bins_ = math.floor(len(x) / binsize)
            bin_means, bin_edges, binnumber = stats.binned_statistic(
                x, y, statistic="median", bins=bins_)

            bin_width = bin_edges[1] - bin_edges[0]
            bin_centers = bin_edges[1:] - bin_width / 2

            temp = []

            for i in range(len(bin_centers)):
                temp.append(bin_centers[i] - bin_centers[0])

            bin_centers = temp

            return (bin_centers, bin_means)

        # Increase SNR by smoothening the data
        def smoothenedPoints(self):
            smooth_box_width = 15
            smoothened_signal = convolve(
                self.rebinnedPoints()[1], Box1DKernel(smooth_box_width))
            smoothened_signal = np.nan_to_num(smoothened_signal)

            return smoothened_signal

        # Locate all local minima and maxima by brute force
        def allminMaxPoints(self):
            y_smooth = self.smoothenedPoints()

            minm = (np.diff(np.sign(np.diff(y_smooth))) > 0).nonzero()[0] + 1
            maxm = (np.diff(np.sign(np.diff(y_smooth))) < 0).nonzero()[0] + 1

            return (minm, maxm)

        # Locate relatively good minima and maxima by employing functions from scipy
        def specificMinMaxPoints(self):
            y_smooth = self.smoothenedPoints()

            order_ = 10

            minm = argrelmin(y_smooth, order=order_)
            minm = minm[0]

            maxm = argrelmax(y_smooth, order=order_)
            maxm = maxm[0]

            return(minm, maxm)

        # Calculate background- An approach by Gourav and Sarthak
        def backgroundCalculator_approach1(self):
            badarr = []
            minm, maxm = np.asarray(self.specificMinMaxPoints())

            # Stores the x values of the maxima
            x = np.asarray(self.rebinnedPoints()[0])
            y_smooth = np.asarray(self.smoothenedPoints())

            for i in range(len(minm) - 1):
                for j in x[maxm]:
                    if x[minm][i] < j < x[minm][i + 1]:
                        badarr.append(np.arange(x[minm][i], x[minm][i + 1]))

            bad = []
            for i in range(len(badarr)):
                bad = np.concatenate((bad, badarr[i]), axis=0)
            bkg = y_smooth.copy()

            for i in range(len(bkg)):
                if bkg[i] in bad:
                    bkg.remove[i]
            background = np.median(bkg)

            return (background, bkg)

        # Calculate background- An approach by Chirag
        def backgroundCalculator_approach2(self):
            x = np.asarray(self.rebinnedPoints()[0])
            y = np.asarray(self.rebinnedPoints()[1])

            tolerance = 7
            df_noise = pd.DataFrame({"x": x, "y": y})

            for i in range(tolerance):
                df_noise = pd.DataFrame(
                    {"x": df_noise["x"], "y": df_noise["y"]})
                mean = df_noise["y"].mean()
                std = df_noise["y"].std()
                df_noise = df_noise.drop(
                    df_noise[(df_noise['y'] >= mean + std)].index)

            noise_mean = df_noise["y"].mean()
            noise_std = df_noise["y"].std()

            return (noise_mean, noise_std)


        # SIDE NOTE: There does not exist a considerable difference between the two background calculation algorithms.
        # Either can be tuned to other by changing the confidence interval estimation appropriately.

        # Removing datapoints that lie below mean+1*std margin
        def dataRemover(self):
            minm, maxm = np.asarray(self.specificMinMaxPoints())
            std = np.std(self.backgroundCalculator_approach1()[1])
            background = self.backgroundCalculator_approach1()[0]
            y_smooth = self.smoothenedPoints()

            i = 0
            while i < len(maxm):
                if maxm[i] < (background * std):
                    maxm = np.delete(maxm, i)
                i += 1

            i = 0
            while i < len(maxm):
                if minm[i] < (background):
                    minm = np.delete(minm, i)
                i += 1

            for i in range(len(y_smooth)):
                if y_smooth[i] < background:
                    y_smooth[i] = background

            return (minm, maxm, y_smooth)

        # Find potential flares and fit them using CHebyshev polynomials (as in plotter.py)
        def flareFinder(self):
            y_smooth = self.dataRemover()[2]
            background = self.backgroundCalculator_approach1()[0]

            temp = []
            for i in range(len(y_smooth)):
                if np.round(background) < y_smooth[i] < np.round(background) + 1:
                    temp.append(i)
            # print(y_smooth, len(y_smooth), background, len(arr))

            start = []
            end = []

            i = 0

            while i < len(temp) - 1:
                if (temp[i] + 1) != temp[i + 1]:
                    start.append(temp[i])
                    end.append(temp[i + 1])
                i += 1

            return (start, end)
