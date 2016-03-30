import numpy as np, pandas as pd, matplotlib.pyplot as plt, sys

def indexSelection(ifile1, ifile2):
    df1 = pd.read_csv(ifile1, skipinitialspace=True)
    df2 = pd.read_csv(ifile2, skipinitialspace=True)
    del df1["#"]
    del df2["#"]
    df1, df2 = df1.sort(["Job_ID"], ascending=[True]), df2.sort(["Job_ID"], ascending=[True])
    del df2["Job_ID"]
    global total
    total = pd.concat([df1,df2]).dropna(axis=1, how="all")
    global headers
    headers = {}
    i = 0
    for item in total:
        headers[i] = item
        i += 1
    for item in headers:
        print(item, headers[item])
    total = pd.concat([df1,df2], axis=1)

def createScatter(col1, col2, ofolder):
    val1 = headers[col1]
    val2 = headers[col2]
    df1 = total[val1]
    df2 = total[val2]
    f, ax = plt.subplots()
    i = 0
    for item in df1:
        try:
            ax.scatter(df1[i], df2[i])
        except KeyError:
            break
        i += 1
    plt.show()

##indexSelection("D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/AllCombinedResults.csv", "D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/AllDerivedResults.csv")
##createScatter(22, 25, "D:/USB/Total Backup/Things/Programming/EnsimsCoding/run")

indexSelection(sys.argv[1], sys.argv[2])
createScatter(sys.argv[1], sys.argv[2], sys.argv[3])