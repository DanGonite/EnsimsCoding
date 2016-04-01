import numpy as np, matplotlib.pyplot as plt, pandas as pd, math, sys

def Hist(ifile, ofolder):
    df = pd.read_csv(ifile).ix[:, 3:]
    fig, axes = plt.subplots(nrows=math.floor(math.sqrt(len(df.columns))), ncols=math.floor(math.sqrt(len(df.columns))), sharey=True, sharex = True)
    figure, axs = plt.subplots(nrows=1, ncols=1, sharey=True, sharex = True)
    dflist = [col for col in df.columns]
    x = 0
    for ax in axes.ravel():
        filename = dflist[x][5::]
        filename2 = ""
        for letter in filename:
            if letter == "[":
                break
            else:
                filename2 += letter
        ax.hist(df[dflist[x]], bins=np.arange(0,(math.floor(math.sqrt(len(df.columns)))*1000),200))
        ax.set_xlabel("Hours"); ax.set_ylabel("Frequency")
        ax.set_title(filename2)
        axs.cla()
        axs.hist(df[dflist[x]], bins=np.arange(0,(math.floor(math.sqrt(len(df.columns)))*1000),200))
        axs.set_xlabel("Hours"); axs.set_ylabel("Frequency")
        axs.set_title(filename2)
        axs.figure.savefig(ofolder+"/"+filename2+".png", format="png")
        x += 1
    plt.show()

Hist(sys.argv[1], sys.argv[2])
#Hist("C:/Users/Jurong/EnsimsCoding/run/SimResults.csv", "run")
#Hist("D:/USB/Total Backup/Things/Programming/EnsimsCoding/run/SimResults.csv", "D:/USB/Total Backup/Things/Programming/EnsimsCoding/run")
