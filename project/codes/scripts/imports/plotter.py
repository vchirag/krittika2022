def main():
    print("RUN main.py")


if __name__ == "__main__":
    main()

else:
    import matplotlib.pyplot as plt
    import numpy as np

    class rawLightCurvePlotter():
        def __init__(self, x, y, title):
            self.x = x
            self.y = y
            self.title = title

        def rawPlotter(self):
            plt.rcParams.update({'font.size': 16})
            plt.figure(figsize=(30, 10))
            plt.plot(self.x, self.y)
            plt.title(self.title)
            plt.xlabel("TIME")
            plt.ylabel("RATE")
            plt.savefig("../data/output/rawPlot", format="svg", dpi=300)

    class rebinnedLightCurvePlotter():
        def __init__(self, x, y, title):
            self.x = x
            self.y = y
            self.title = title

        def rebinPlotter(self):
            plt.rcParams.update({'font.size': 16})
            plt.figure(figsize=(30, 10))
            plt.xticks(np.arange(0, max(self.x), 5000))
            plt.grid()
            plt.plot(self.x, self.y)
            plt.title(self.title)
            plt.xlabel("TIME")
            plt.ylabel("RATE")
            ax = plt.gca()
            for spine in ['top', 'right']:
                ax.spines[spine].set_visible(False)
            ax.spines['left'].set_position(('data', 0))
            plt.savefig("../data/output/rebinnedPlot", format="svg", dpi=300)

    class smoothenedLightCurvePlotter():
        def __init__(self, x, y, title):
            self.x = x
            self.y = y
            self.title = title

        def smoothPlotter(self):
            plt.rcParams.update({'font.size': 16})
            plt.figure(figsize=(30, 10))
            plt.xticks(np.arange(0, max(self.x), 5000))
            plt.grid()
            plt.plot(self.x, self.y)
            plt.title(self.title)
            plt.xlabel("TIME")
            plt.ylabel("RATE")
            ax = plt.gca()
            for spine in ['top', 'right']:
                ax.spines[spine].set_visible(False)
            ax.spines['left'].set_position(('data', 0))
            plt.savefig("../data/output/smoothPlot", format="svg", dpi=300)

    class minimaMaximaPlotter():
        def __init__(self, x, y, minimaX, minimaY, maximaX, maximaY, title):
            self.x = x
            self.y = y
            self.minimaX = minimaX
            self.minimaY = minimaY
            self.maximaX = maximaX
            self.maximaY = maximaY
            self.title = title

        def minMaxPlotter(self):
            plt.rcParams.update({'font.size': 16})
            plt.figure(figsize=(30, 10))
            plt.xticks(np.arange(0, max(self.x), 5000))
            plt.grid()
            plt.plot(self.x, self.y, color="grey")
            plt.plot(self.minimaX, self.minimaY,
                     "x", label="minima", color="r")
            plt.plot(self.maximaX, self.maximaY,
                     "x", label="maxima", color="b")
            plt.title(self.title)
            plt.xlabel("TIME")
            plt.ylabel("RATE")
            ax = plt.gca()
            for spine in ['top', 'right']:
                ax.spines[spine].set_visible(False)
            ax.spines['left'].set_position(('data', 0))
            plt.savefig("../data/output/minimaMaximaPlot",
                        format="svg", dpi=300)
