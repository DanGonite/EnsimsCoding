import pandas as pd, matplotlib.pyplot as plt

def createScatterPlot(ifile1, ifile2, x, y):
    df1 = pd.read_csv(ifile1)
    df2 = pd.read_csv(ifile2)
    dfMaster = pd.concat([df1, df2])
    #x = x for x in 
    plt.scatter(x,y, s=10)
    plt.show()
    
createScatterPlot("C:/Users/Jurong/EnsimsCoding/run/AllDerivedResults.csv","C:/Users/Jurong/EnsimsCoding/run/AllCombinedResults.csv",10,10)