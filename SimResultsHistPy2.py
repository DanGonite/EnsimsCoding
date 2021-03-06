import matplotlib.pyplot as plt, pandas as pd, sys, math

def Hist(ifile):
    plt.close("all")
    df = pd.read_csv(ifile).ix[:, 3:]
    dflist = pd.DataFrame.to_dict(df)
    i = 0
    maxlist = []
    for item in dflist:
        for val in dflist[item]:
            try:
                maxlist.append(float(dflist[item][val]))
            except ValueError:
                pass
    subsizex = int(math.sqrt(len(df.columns)))
    subsizey = int(math.sqrt(len(df.columns)))
    for column in df.columns:
        plt.subplot(subsizex, subsizey,i+1)
        x = []
        x.append(df[[column]])
        plt.hist(x)
        plt.axis([0, max(maxlist), 0, 50])
        plt.xlabel('Hours')
        plt.ylabel('Frequency')
        plt.title(column)
        plt.grid(True)
        i += 1
    plt.show()

Hist(sys.argv[1])
