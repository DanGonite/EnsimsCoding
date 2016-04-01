import numpy as np, pandas as pd, matplotlib.pyplot as plt, sys

df = pd.read_csv("C:\\Users\\Yi\\EnsimsCoding\\run\\AllCombinedResults.csv", skipinitialspace=True)
df = df.sort(["Job_ID"])

print(df["@@building_fabrics@@"].dtype.name)

if df["@@building_fabrics@@"].dtype.name == "category":
    print("Yay")

col1 = "c3: Cooling:DistrictCooling [J](RunPeriod)"

df1 = df["@@building_fabrics@@"].value_counts()

print(df1.value_counts()[df1.value_counts() == 1])

if df1.value_counts()[df1.value_counts() == 1].empty == True:
    print ("Yay")

df1 = df1.sort_index()

cat = df1.index.tolist()

f, ax = plt.subplots()

i=0
for item in df["@@building_fabrics@@"]:
    ax.scatter((cat.index(item)+1), df[col1][i])
    i+=1


cat.insert(0, "")
plt.xticks(np.arange(len(cat)), cat)
plt.show()
