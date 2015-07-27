import numpy as np, matplotlib.pyplot as plt, pandas as pd, math

df = pd.read_csv("C:/Users/Jurong/EnsimsCoding/run/SimResults.csv").ix[:, 3:]
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
    axs.figure.savefig("C:/Users/Jurong/EnsimsCoding/run/"+filename+".png", format="png")
    x += 1