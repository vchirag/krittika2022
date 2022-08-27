def main():
    print("RUN main.py")


def plotter(x, y, date, flag):

    fig, ax = plt.subplots()

    fig.set_figheight(4)
    fig.set_figwidth(15)

    ax.set_xlabel("Time")
    ax.set_ylabel("Rate")

    ax.xaxis.grid()
    ax.yaxis.grid()

    if flag == 0:
        title_ = str(date) + "- Raw Plot"
        ax.set_title(title_)
        ax.plot(x, y)
        plt.savefig("../data/output/rawPlot", format="png")

    if flag == 1:
        title_ = str(date) + "- Rebinned Plot"
        ax.set_xlim(0, 86400)
        ax.set_xticks(np.arange(0, 87000, 5000))
        ax.set_title(title_)
        ax.plot(x, y)
        plt.savefig("../data/output/rebinnedPlot", format="png")

    if flag == 2:
        title_ = str(date) + "- Smoothened Plot"
        ax.set_xlim(0, 86400)
        ax.set_xticks(np.arange(0, 87000, 5000))
        ax.set_title(title_)
        ax.plot(x, y)
        plt.savefig("../data/output/smoothenedPlot", format="png")


def minMaxPlotter(x, y, minimaX, minimaY, maximaX, maximaY, date, flag):
    fig, ax = plt.subplots()

    fig.set_figheight(4)
    fig.set_figwidth(15)

    ax.set_xlabel("Time")
    ax.set_ylabel("Rate")

    ax.xaxis.grid()
    ax.yaxis.grid()

    ax.set_xlim(0, 86400)
    ax.set_xticks(np.arange(0, 87000, 5000))

    if flag == 3:
        title_ = str(date) + "- All labelled minima and maxima"
        ax.set_title(title_)
        ax.plot(x, y, color="grey")
        ax.scatter(minimaX, minimaY, marker="x", color="red")
        ax.scatter(maximaX, maximaY, marker="x", color="green")
        plt.savefig("../data/output/allMinMaxPlot", format="png")

    if flag == 4:
        title_ = str(date) + "- Specifically labelled minima and maxima"
        ax.set_title(title_)
        ax.plot(x, y, color="grey")
        ax.scatter(minimaX, minimaY, marker="x", color="red")
        ax.scatter(maximaX, maximaY, marker="x", color="green")
        plt.savefig("../data/output/specificMinMaxPlot", format="png")


def bkgPlotter(x, y, minimaX, minimaY, maximaX, maximaY, bkg, date, flag):
    fig, ax = plt.subplots()

    fig.set_figheight(4)
    fig.set_figwidth(15)

    ax.set_xlabel("Time")
    ax.set_ylabel("Rate")

    ax.xaxis.grid()
    ax.yaxis.grid()

    ax.set_xlim(0, 86400)
    ax.set_xticks(np.arange(0, 87000, 5000))

    if flag == 5:
        title_ = str(date) + "- Background (Gaurav and Sarthak)"
        ax.axhline(bkg)
        ax.plot(x, y, color="grey")
        ax.scatter(minimaX, minimaY, marker="x", color="red")
        ax.scatter(maximaX, maximaY, marker="x", color="green")
        ax.set_title(title_)
        plt.savefig("../data/output/bkgMethod1", format="png")

    if flag == 6:
        title_ = str(date) + "- Background (Chirag)"
        ax.fill_between(x, (bkg[0] + 2 * bkg[1]),
                        (bkg[0] - 2 * bkg[1]), alpha=0.4)
        ax.plot(x, y, color="grey")

        ax.scatter(minimaX, minimaY, marker="x", color="red")
        ax.scatter(maximaX, maximaY, marker="x", color="green")
        ax.set_title(title_)
        plt.savefig("../data/output/bkgMethod2", format="png")


def noBkgPlotter(x, y, minimaX, minimaY, maximaX, maximaY, date, flag):
    fig, ax = plt.subplots()

    fig.set_figheight(4)
    fig.set_figwidth(15)

    ax.set_xlabel("Time")
    ax.set_ylabel("Rate")

    ax.xaxis.grid()
    ax.yaxis.grid()

    ax.set_xlim(0, 86400)
    ax.set_xticks(np.arange(0, 87000, 5000))

    if flag == 7:
        title_ = str(date) + "- Removed Background"
        ax.set_title(title_)
        ax.plot(x, y, color="grey")
        ax.scatter(minimaX, minimaY, marker="x", color="red")
        ax.scatter(maximaX, maximaY, marker="x", color="green")
        plt.savefig("../data/output/removedBkg", format="png")


def flarePlotter(n, x, y, start, end, date):

    title_ = str(date) + "- Detected Flares"
    plt.rcParams.update({'font.size': 8})

    if (n % 2 == 0):
        rows = round(n / 2)
        cols = 2
    if (n % 2 != 0):
        rows = round(n / 2) + 1
        cols = 2

    fig, ax = plt.subplots(rows, cols)

    for i in range(rows):
        for j in range(cols):
            tStart = start[2 * i + j]
            tEnd = end[2 * i + j]

            x_eff = x[tStart:tEnd]
            y_eff = y[tStart:tEnd]
            p = np.polynomial.Chebyshev.fit(x_eff, y_eff, 15)

            ax[i, j].plot(x_eff, p(x_eff), "r", linewidth=0.5,
                          label="15th order Chebyshev fit")
            ax[i, j].plot(x_eff, y_eff, "b-", linewidth=0.7, label="data")

            ax[i, j].xaxis.grid()
            ax[i, j].yaxis.grid()

            ax[i, j].set_xlabel('Time (s)')
            ax[i, j].set_ylabel('Rate')

            ax[i, j].legend(loc='best')

    fig.suptitle(title_)

    plt.savefig("../data/output/identifiedFlares", format="png")


if __name__ == "__main__":
    main()


else:
    import matplotlib.pyplot as plt
    import numpy as np
