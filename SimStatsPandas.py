import pandas as pd, sys

def getSimStats(ifile, ofile):
    df = pd.read_csv(ifile)
    col = []
    for column in df:
        if column!= "#":
            col.append(column)
    df = df[col].describe().transpose()
    col = []
    for stat in df:
        if stat == "mean" or stat == "min" or stat == "max" or stat == "std":
            col.append(stat)
    df = df[col].transpose()
    df.insert(0, "Time/Date", "")
    df.insert(0, "Job_ID", "")
    df.to_csv(ofile)

##getSimStats(sys.argv[1], sys.argv[2])
getSimStats("run/SimResults.csv", "run/SimStatsPandas.csv")