import numpy as np, pandas as pd, matplotlib.pyplot as plt

def createScatter(ifile1, col1, ifile2, col2, ofolder):
    df1 = pd.read_csv(ifile1)
    df2 = pd.read_csv(ifile2)
    f, ax = plt.subplots()
    df3 = df1[col1]
    df4 = df2[col2]
    print (type(df3))

    i = 0
    for item in df3:
        print (df3[i])
        print (df4[i])
        print ("")
        ax.scatter(df3[i], df4[i])
        i += 1

    col1name = col1.replace(":", "")
    col2name = col2.replace(":", "")
    fname = col1name + " - " + col2name
    ax.set_title(fname)
    ax.figure.savefig(ofolder+"/"+fname+".png", format="png")

    plt.show()

createScatter("D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/AllCombinedResults.csv", "c2: Heating:DistrictHeating [J](RunPeriod)", "D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/AllDerivedResults.csv", "t1: Heating [kWh]", "D:/USB/Total Backup/Things/Programming/EnsimsCoding/run")

##createScatter(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])