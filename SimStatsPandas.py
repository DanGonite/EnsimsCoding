import pandas as pd, sys

def getSimStats(ifile, ofile):
    df = pd.read_csv(ifile).describe().drop('#', 1)
    # This
##    df.insert(0, "Time/Date", "")
##    df.insert(0, "Job_ID", "")
    # Or this
    df.insert(0, "Time/Date", ""); df.insert(0, "Job_ID", "")
    df.to_csv(ofile)

getSimStats(sys.argv[1], sys.argv[2])