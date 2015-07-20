import pandas as pd, sys

def getSimStats(ifile, ofile):
    df = pd.read_csv(ifile)
    col = []
    for column in df:
        if column!= "#":
            col.append(column)
    df = df[col].describe()
    df.insert(0, "Time/Date", "")
    df.insert(0, "Job_ID", "")
    df.to_csv(ofile)

getSimStats(sys.argv[1], sys.argv[2])