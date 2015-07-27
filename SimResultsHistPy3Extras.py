import numpy as np, matplotlib.pyplot as plt, pandas as pd, math, sys

def Hist(ifile, ofolder):
    df = pd.read_csv(ifile).ix[:, 3:]
    size = math.floor(math.sqrt(len(df.columns)))
    x = 0
    fig, axes = plt.subplots(nrows=size, ncols=size, sharey=True, sharex = True)
    figure, axs = plt.subplots(nrows=1, ncols=1, sharey=True, sharex = True)
    
    dflist = [col for col in df.columns]
    numbins = np.arange(0,(size*1000),200)
    
    for ax in axes.ravel():
        filename = dflist[x][5::]
        ax.hist(df[dflist[x]], bins=numbins)
        ax.set_xlabel("Hours")
        ax.set_ylabel("Frequency")
        axs.cla()
        axs.hist(df[dflist[x]], bins=numbins)
        axs.figure.savefig(ofolder+filename+".png", format="png")
        x += 1

# Hist(sys.argv[1], sys.argv[2])
Hist("C:/Users/Jurong/EnsimsCoding/run/SimResults.csv", "C:/Users/Jurong/EnsimsCoding/run/")