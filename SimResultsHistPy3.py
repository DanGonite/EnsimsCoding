import pandas as pd, matplotlib.pyplot as plt, numpy as np, math, sys, matplotlib.pylab as lab

def Hist(ifile):
    df = pd.read_csv(ifile).ix[:, 3:]
    size=math.floor(math.sqrt(len(df.columns)))
    df.hist(color="k", alpha=0.5, bins=np.arange(0,(size*1000),200), normed=False, sharex=True, sharey=True, figsize=(14.2,8), layout=(size,size))
    plt.show()
    
#Hist(sys.argv[1])
Hist('run/SimResults.csv')
