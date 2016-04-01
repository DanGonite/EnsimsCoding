import numpy as np, pandas as pd, matplotlib.pyplot as plt, sys

def indexSelection(ifile1, ifile2):
    # Takes and prepares csv files #
    df1 = pd.read_csv(ifile1, skipinitialspace=True)
    df2 = pd.read_csv(ifile2, skipinitialspace=True)
    for i in range(2):
        i += 1
        del locals()["df" + str(i)]["#"]
        locals()["df"+str(i)] = locals()["df"+str(i)].sort(["Job_ID"], ascending=[True])
    del df2["Job_ID"]
    global total
    total = pd.concat([df1, df2]).dropna(axis=1, how="all")
##    print(total)
##    for item in total:
##        total = total[total[item].apply(lambda x: type(x) in [int, np.int64, float, np.float64])]
##    print(total)
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

def createScatter(col1, col2, ofolder):
    try:
        df1 = total[headers[col1]]
        df2 = total[headers[col2]]
    except KeyError:
        xCol = input("One of your colums was invalid, please select a valid column:")
        yCol = input("Please choose a valid column that you would like to plot the first column against:")
        createScatter(int(xCol), int(yCol), ofolder)
    # Creates graphs #
    f, ax = plt.subplots()
    i = 0
    for item in df1:
        ax.scatter(df1[i], df2[i])
        i += 1
    # Formats and saves graphs #
    fname = (headers[col1] + " - " + headers[col2]).replace(":", "")
    ax.set_xlabel(headers[col1]); ax.set_ylabel(headers[col2])
    try:
        ax.figure.savefig(ofolder + "/" + fname + ".png", format = "png")
    except IOError:
        ofile = input("The previous path was invalid, please enter a new path:")
        createScatter(col1, col2, ofile)
    plt.show()

indexSelection("D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/AllCombinedResults.csv", "D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/AllDerivedResults.csv")
xCol = input("Please choose a column:")
yCol = input("Please choose the column that you would like to plot the first column against:")
ofile = input("Please enter a path to the folder in which you would like to save your graph:")
createScatter(int(xCol), int(yCol), ofile)