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
    global total, headers
    total = pd.concat([df1, df2]).dropna(axis=1, how="all")
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
    try:
        head1 = headers[xCol]
        head2 = headers[yCol]
    except KeyError:
        xCol = input("One of your colums was invalid, please select a valid column: ")
        yCol = input("Please choose a valid column that you would like to plot the first column against: ")
        checkCategorical(int(xCol), int(yCol))
    global fname
    fname = (headers[xCol] + " - " + headers[yCol]).replace(":", "")
    if "@@" not in head1 and "File" not in head1:
        if "@@" not in head2 and "File" not in head2:
            createScatter(xCol, yCol)
        else:
            createCatScatter(yCol, xCol)
    else:
        createCatScatter(xCol, yCol)

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

def createScatter(xCol, yCol):
    df1 = total[headers[xCol]]
    df2 = total[headers[yCol]]
    # Creates graphs #
    i = 0
    for item in df1:
        ax.scatter(df1[i], df2[i])
        i += 1
    # Formats and saves graphs #
    ax.set_xlabel(headers[xCol]); ax.set_ylabel(headers[yCol])
    saveFig(ofile)

def createCatScatter(xCol, yCol):
    df1 = total[headers[xCol]].value_counts().sort_index()
    df2 = total[headers[yCol]]
    cat = df1.index.tolist()
    cat.insert(0, "")
    cat.append("")
    i=0
    for item in total[headers[xCol]]:
        ax.scatter((cat.index(item)), total[headers[yCol]][i])
        i+=1
    plt.xticks(np.arange(len(cat)), cat)
    ax.set_xlabel(headers[xCol]); ax.set_ylabel(headers[yCol])
    saveFig(ofile)

def saveFig(ofolder):
    try:
        ax.figure.savefig(ofolder + "/" + fname + ".png", format = "png")
    except IOError:
        ofile = input("The previous path was invalid, please enter a new path: ")
        saveFig(ofile)

f, ax = plt.subplots()
indexSelection("D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/AllCombinedResults.csv", "D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/AllDerivedResults.csv")
xCol = input("Please choose a column: ")
yCol = input("Please choose the column that you would like to plot the first column against: ")
ofile = input("Please enter a path to the folder in which you would like to save your graph: ")
checkCategorical(int(xCol), int(yCol))
plt.show()