import sys
import pandas as pd

df =pd.read_csv(sys.argv[1])

#insight1: year that had higehst avg suicide rate 
avg_by_year = df.groupby('YEAR_NUM')['ESTIMATE'].mean()
worst_year_idx=avg_by_year.idxmax()

f1=open("insight1.txt","w")
f1.write("Avarage estimate by year:\n")
for year,val in avg_by_year.items():
    f1.write(str(round(year,2))+":"+str(round(val,4))+"\n")
f1.write("\nYear with highest average estimate index: " + str(round(worst_year_idx, 2)) + "\n")
f1.close()

#insight2: dist of pc1 bins
bins=df['PC1_binned'].value_counts().sort_index()

f2 = open("insight2.txt", "w")
f2.write("PC1 bin distribution (0=low,1=mid,2=high):\n")
for bin_val, count in bins.items():
    f2.write(str(bin_val) + ": " + str(count) + "\n")
f2.close()

#insight3: corr between etimate and age
corr= df[['ESTIMATE','AGE_NUM','YEAR_NUM','STUB_NAME_NUM']].corr()

f3=open("insight3.txt","w")
f3.write("Correlation with estimate:\n")
for col in ['AGE_NUM','YEAR_NUM','STUB_NAME_NUM']:
    val=corr.loc['ESTIMATE',col]
    f3.write(col+":"+str(round(val,4))+"\n")
f3.close()

print("Insights generated and saved to insight1.txt, insight2.txt, and insight3.txt")

import os
os.system("python visualize.py data_preprocessed.csv")