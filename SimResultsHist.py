import matplotlib.pyplot as plt, pandas as pd, sys

def Hist(ifile):
    plt.close("all")
    df = pd.read_csv("run/SimResults.csv")
    df = df.ix[:, 3:]
    dflist = pd.DataFrame.to_dict(df)
    i = 0
    maxlist = []
    for item in dflist:
        for val in dflist[item]:
            key = dflist[item]
            try:
                maxlist.append(float(key[val]))
            except ValueError:
                pass
    maxi = max(maxlist)
    for column in df.columns:
        plt.subplot(4,4,i+1)
        x = []
        x.append(df[[column]])
        y = 0 * len(x)
        plt.hist(x)
        plt.axis([0, maxi, 0, 50])
        plt.xlabel('Hours')
        plt.ylabel('Frequency')
        plt.title(column)
        plt.grid(True)
        i += 1
    plt.show()

Hist(sys.argv[1])