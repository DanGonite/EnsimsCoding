import pandas as pd, sys

def getSimStats(ifile, ofile):
    df = pd.read_csv(ifile)
    col = []
    for column in df:
        if column!= "#":
            col.append(column)
    df = df[col]
    df.describe().to_csv(ofile)

##getSimStats(sys.argv[1], sys.argv[2])
getSimStats("run//SimResults.csv", "run//SimStatsPandas.csv")