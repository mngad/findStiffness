import os
import pandas
import pyperclip as pc
import re

def findStiffness(segSize, incrSize, plot, fileDir):
    allRes = ''
    os.chdir(fileDir)
     # Scan through them separating them.
    listOfFolderNames = os.listdir(fileDir)
    listOfFolderNames.sort() #sort alphabetically  - important for plotting
    graphList = []
    graphList.append([])
    pltCount = 0

    #find limits of plot ie. > 50 N to max
    for folder in listOfFolderNames:
        s =[]
        MaxS =0
        lower = 0
        upper = 0
        m=0
        fileLoc =  folder + '/Specimen_RawData_1.csv'
        data = pandas.read_csv(fileLoc,header = 1)

        countr =0
        load = list(data['(N)'])
        for i in load: # removes the cycling preload from the data
            if(i<=51):
                lower = countr
            countr = countr + 1

        xdata = data['(mm)']
        ydata = data['(N)']
        x = xdata.tolist()
        y = ydata.tolist()
        x = x[lower:]
        y = y[lower:]
        xmin = x[0]
        ymin = y[0]
        fail = False
        c=0
        for i in range(len(x)):# starts the data at 0 not 50
            diff =  x[i] - xmin
            x[i] = diff

        for i in range(len(x)): # finds an appropriate starting point so that the last segment is always up to the end of the data
            c = c + 1
            if ((len(x)-1)-(incrSize*c)-segSize)<(incrSize):# the -1 is there due to array starting at 0 -> e.g. len(x) =56; but x-56= is out of bounds :)
                aa =len(x)-(incrSize*c)-1-segSize
                break

        while (aa+segSize+incrSize) < len(x):
            s.append((y[aa + segSize]-y[aa])/(x[aa+segSize]-x[aa]))
            aa = aa +incrSize

        if(plot == True):
            graphList[pltCount].append(x)
            graphList[pltCount].append(y)
            graphList[pltCount].append(folder)
            graphList.append([])
            pltCount = pltCount + 1



        MaxS =max(s)
        if(MaxS>s[-1:]):
            fail = True
        Mindex = s.index(max(s))
        #allRes = allRes + str(segSize) + ', ' + folder[:-16] + ', ' + str(MaxS) + ', fail = ' + str(fail) +  '\n'
        allRes = allRes + folder[:-16] + ', ' + str(MaxS) + ', fail = ' + str(fail) + '\n'

    print(allRes)
    pc.copy(allRes)
    return(graphList)
    print('Results copies to clipboard')


