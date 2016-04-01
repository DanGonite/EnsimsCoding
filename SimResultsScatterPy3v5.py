import numpy as np, pandas as pd, matplotlib.pyplot as plt, sys

def indexSelection(ifile1, ifile2):
    # Takes and prepares csv files #
    df1 = pd.read_csv(ifile1, skipinitialspace=True)
    df2 = pd.read_csv(ifile2, skipinitialspace=True)
    for i in range(2):
        i += 1
        del locals()["df" + str(i)]["#"]
        locals()["df"+str(i)] = locals()["df"+str(i)].sort(["Job_ID"])
    del df2["Job_ID"]
    global total
    total = pd.concat([df1, df2]).dropna(axis=1, how="all")
    global headers
    # Creates list of headers #
    headers = {}
    i = 0
    for item in total:
        headers[i] = item
        i += 1
    for item in headers:
        print(item, headers[item])
    total = pd.concat([df1, df2], axis=1)

def checkCategorical(xCol, yCol):
    head1 = headers[xCol]
    head2 = headers[yCol]
    if "@@" not in head1 and "File" not in head1:
        if "@@" not in head2 and "File" not in head2:
            createScatter(xCol, yCol, ofile)
        else:
            createCatScatter(yCol, xCol, ofile)
    else:
        createCatScatter(xCol, yCol, ofile)
        
    #try:
    #    df1 = total[headers[xCol]]
    #    df2 = total[headers[yCol]]
    #except KeyError:
    #    xCol = input("One of your colums was invalid, please select a valid column:")
    #    yCol = input("Please choose a valid column that you would like to plot the first column against:")
    #    checkCategorical(int(xCol), int(yCol))
    #df1 = df1.value_counts()
    #df2 = df2.value_counts()
    #if df1.value_counts()[df1.value_counts() == 1].empty == False:
    #    if df2.value_counts()[df2.value_counts() == 1].empty == False:
    #        createScatter(xCol, yCol, ofile)
    #    else:
    #        createCatScatter(yCol, xCol, ofile)
    #else:
    #    createCatScatter(xCol, yCol, ofile)

def createScatter(xCol, yCol, ofolder):
    try:
        df1 = total[headers[xCol]]
        df2 = total[headers[yCol]]
    except KeyError:
        xCol = input("One of your colums was invalid, please select a valid column:")
        yCol = input("Please choose a valid column that you would like to plot the first column against:")
        checkCategorical(int(xCol), int(yCol))
    # Creates graphs #
    f, ax = plt.subplots()
    i = 0
    for item in df1:
        ax.scatter(df1[i], df2[i])
        i += 1
    # Formats and saves graphs #
    fname = (headers[xCol] + " - " + headers[yCol]).replace(":", "")
    ax.set_xlabel(headers[xCol]); ax.set_ylabel(headers[yCol])
    try:
        ax.figure.savefig(ofolder + "/" + fname + ".png", format = "png")
    except IOError:
        ofile = input("The previous path was invalid, please enter a new path:")
        checkCategorical(xCol, yCol, ofile)

def createCatScatter(xCol, yCol, ofolder):
    try:
        df1 = total[headers[xCol]]
        df2 = total[headers[yCol]]
    except KeyError:
        xCol = input("One of your colums was invalid, please select a valid column:")
        yCol = input("Please choose a valid column that you would like to plot the first column against:")
        checkCategorical(int(xCol), int(yCol))
    df1 = df1.value_counts()
    df1 = df1.sort_index()
    cat = df1.index.tolist()
    cat.insert(0, "")
    cat.append("")
    f, ax = plt.subplots()
    i=0
    for item in total[headers[xCol]]:
        ax.scatter((cat.index(item)), total[headers[yCol]][i])
        i+=1
    plt.xticks(np.arange(len(cat)), cat)
    fname = (headers[xCol] + " - " + headers[yCol]).replace(":", "")
    ax.set_xlabel(headers[xCol]); ax.set_ylabel(headers[yCol])
    try:
        ax.figure.savefig(ofolder + "/" + fname + ".png", format = "png")
    except IOError:
        ofile = input("The previous path was invalid, please enter a new path:")
        createScatter(xCol, yCol, ofile)

indexSelection("D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/AllCombinedResults.csv", "D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/AllDerivedResults.csv")
xCol = input("Please choose a column:")
yCol = input("Please choose the column that you would like to plot the first column against:")
ofile = input("Please enter a path to the folder in which you would like to save your graph:")
checkCategorical(int(xCol), int(yCol))
plt.show()