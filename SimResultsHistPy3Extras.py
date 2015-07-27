import numpy as np, matplotlib.pyplot as plt, pandas as pd, math, sys

def Hist(ifile, ofolder):
    df = pd.read_csv(ifile).ix[:, 3:]
    size = math.floor(math.sqrt(len(df.columns)))
    x = 0
    fig, axes = plt.subplots(nrows=size, ncols=size, sharey=True)
    figure, axs = plt.subplots(nrows=1, ncols=1, sharey=True)
    
    dflist = [col for col in df.columns]
    numbins = np.arange(0,(size*1000)
    
    for ax in axes.ravel():
        filename = dflist[x][5::]
        ax.hist(df[dflist[x]], bins=numbins,200))
        axs.cla()
        axs.hist(df[dflist[x]], bins=numbins,200))
        axs.figure.savefig(ofolder+filename+".png", format="png")
        x += 1

Hist(sys.argv[1], sys.argv[2])