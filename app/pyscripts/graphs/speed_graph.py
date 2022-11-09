def showSpeedGraph(maxParticles):

    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    import numpy as np
    from itertools import count
    import pandas as pd

    fig, ax = plt.subplots()
    fileContentsList = []
    xList = []
    yList = []
    counter = count(0, 1)
    colorOrder = ('b', 'r', 'y', 'g')


    def readFiles(fName, index):
        # reads and returns contents of csv file
        try:
            fileContents = pd.read_csv(r"app/pyscripts/graphs/data_points_csv/{fName}{index}.csv".format(fName=fName, index=index))
        except:
            print("File not found")

        return fileContents


    def getFileContents(numOfParticles, fName):
        # retrieve data points for each particle 
        for particle in range(1, numOfParticles+1):
            fileContents = readFiles(fName, particle)
            fileContentsList.append(fileContents)
            
            # initialise lists for x and y points for each particle
            xList.append([])
            yList.append([])

    def plotAxes(maxParticles):
        # method to plot x and y points to graph
        for index in range(maxParticles):
            ax.plot(xList[index], yList[index])

    # call functions to get data points and initialise axes
    getFileContents(maxParticles, "speed_data")
    plotAxes(maxParticles)


    def update(i):
        # adds points from the x and y column in the csv until there are no more values to add
        try:
            idx = next(counter)
            for i, xPoints in enumerate(xList):
                xPoints.append(fileContentsList[i].iloc[idx, 0])
            for i, yPoints in enumerate(yList):
                yPoints.append(fileContentsList[i].iloc[idx, 1])

            plt.cla()

            for i in range(len(fileContentsList)):
                ax.plot(xList[i], yList[i], color=colorOrder[i])

        except:
            pass

    # create animation of graph, updating at intervals of 100ms
    ani = FuncAnimation(fig=fig, func=update, interval=100)
    plt.show()



