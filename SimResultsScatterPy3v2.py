import numpy as np, pandas as pd, matplotlib.pyplot as plt

ifile1 = "D:/USB/Things/Programming/EnsimsCoding/run/AllDerivedResults.csv"
ifile2 = "D:/USB/Things/Programming/EnsimsCoding/run/AllCombinedResults.csv"
df1 = pd.read_csv(ifile1)
df2 = pd.read_csv(ifile2)
dfMaster = pd.concat([df1, df2])
dflist = [col for col in dfMaster.columns]
f, ax = plt.subplots()

col1 = "c1: InteriorEquipment:Electricity [J](RunPeriod)"
col2 = "s1: Electricity [kWh]"

##for item in dfMaster[col1][::100]:
##    for itemn in dfMaster[col2][::100]:
##        ax.scatter(item, itemn)
##plt.show()
##df3 = np.array([df[col1], df[col2]])
##
##print(df3)

##print(type(df2[col1].iloc[item]))

print(type(df2))

for item in df2[col1]:
    print(type(item.item()))
    print(type(df2[col1].ix(item.item())))
    ax.scatter(item, df2[col1].ix(item))
##df3 = pd.DataFrame(dfMaster[col1])
##df4 = pd.DataFrame(dfMaster[col2])
##print (type(dfMaster[col1][3]))
##print (type(dfMaster[col1])).0
##print (type(dfMaster))
##print (type(df3))
##print (type(df4))
##print (type(df3[col1][3]))
##print (df3[col1][3])
##print (type(float(df3[col1][3])))
##ax.scatter([np.float64(df3[col1][x]) for x in range(len(dflist))], [np.float64(df4[col2][y]) for y in range(len(dflist))])

plt.show()