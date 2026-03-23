import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1]) 

fig, axes=plt.subplots(1,3,figsize=(18,5))

#plot1: histogram of ESTIMATE
df['ESTIMATE'].hist(bins=40,ax=axes[0],color='steelblue')
axes[0].set_title("Distribution of Estimate")
axes[0].set_xlabel("Estimate")
axes[0].set_ylabel("Count")

#plot2:PC1 binned bar chart
df['PC1_binned'].value_counts().sort_index().plot(kind='bar',ax=axes[1], color='coral')
axes[1].set_title("PC1 Bin Counts")
axes[1].set_xlabel("Bin")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis='x', labelrotation=0)

#plot3: corr heatmap
cols=df[['ESTIMATE','AGE_NUM','YEAR_NUM','STUB_NAME_NUM','PC1','PC2']]
sns.heatmap(cols.corr(), annot=True, fmt=".2f", cmap='coolwarm', ax=axes[2])
axes[2].set_title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("summary_plot.png")
print("plot saved")

import os 
os.system("python cluster.py data_preprocessed.csv")