import os
import glob
import pandas as pd

folder_path1 = "./300K"
folder_path3 = "./500K"

file_paths1 = glob.glob(os.path.join(folder_path1, "zaxis*"))
file_paths3 = glob.glob(os.path.join(folder_path3, "zaxis*"))

dfs1 = []
dfs3 = []

for file_path in file_paths1:
    df = pd.read_csv(file_path, skiprows=2, sep=' ', index_col=None, header=None)
    df.drop(int(0), axis=1, inplace=True)
    df.drop(int(2), axis=1, inplace=True)
    dfs1.append(df)

for file_path in file_paths3:
    df = pd.read_csv(file_path, skiprows=2, sep=' ', index_col=None, header=None)
    df.drop(int(0), axis=1, inplace=True)
    df.drop(int(2), axis=1, inplace=True)
    dfs3.append(df)

merged_df1 = pd.concat(dfs1, axis=1)
merged_df3 = pd.concat(dfs3, axis=1)




import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
ax = plt.gca()

numbers_list = [i for i in range(1, 30001, 150)]

c_co_300 = (merged_df1.iloc[36] + merged_df1.iloc[38])/2
c_co2_300 = merged_df1.iloc[37]

c_co_500 = (merged_df3.iloc[36] + merged_df3.iloc[38])/2
c_co2_500 = merged_df3.iloc[37]

plt.plot(numbers_list, c_co_300, c="gray", alpha=0.5, label=r'C (CO) 300K')
plt.plot(numbers_list, c_co2_300, c="royalblue", alpha=0.5, label=r'C (CO$_2$) 300K')

plt.plot(numbers_list, c_co_500, c="black", alpha=0.8, label=r'C (CO) 500K')
plt.plot(numbers_list, c_co2_500, c="orangered", alpha=0.7, label=r'C (CO$_2$) 500K')

current_values = plt.gca().get_xticks()
ax.set_xticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.xlabel('Time (fs)', size=22, labelpad=10)
#plt.xlim(0,1.0)
plt.ylabel('z-coordinate (Å)', size=22, labelpad=10)
plt.ylim(0, 30000)
plt.ylim(0, 30)
plt.yticks(size=16)
plt.xticks(size=16)
plt.legend(loc=4, ncol=2, fontsize=16, frameon=False)
plt.show()
