import numpy as np, pandas as pd, matplotlib.pyplot as plt

def indexSelection(ifile1, ifile2):
    df1 = pd.read_csv(ifile1, skipinitialspace=True)
    df2 = pd.read_csv(ifile2, skipinitialspace=True)
    global total
    total = pd.concat([df1,df2])
    global headers
    headers = {}
    i = 0
    for item in total:
        headers[i] = item
        i += 1
    for item in headers:
        print(item, headers[item])

def createScatter(col1, col2, ofolder):
    val1 = headers[col1]
    val2 = headers[col2]
    df1 = total[val1]
    df2 = total[val2]

    f, ax = plt.subplots()
    i = 0
    for item in df1:
        print(i)
        try:
            ax.scatter(df1[i], df2[i])
        except KeyError:
            break
        i += 1
##
##    col1name = val1.replace(":", "")
##    col2name = val2.replace(":", "")
##    fname = col1name + " - " + col2name
##    ax.set_title(fname)
##    ax.figure.savefig(ofolder+"/"+fname+".png", format="png")

    plt.show()

indexSelection("D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/AllCombinedResults.csv", "D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/AllDerivedResults.csv")

createScatter(23, 27, "D:/USB/Total Backup/Things/Programming/EnsimsCoding/run")

##createScatter(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])