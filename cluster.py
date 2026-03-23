import sys
import pandas as pd
from sklearn.cluster import KMeans

df=pd.read_csv(sys.argv[1])

cols=df[['PC1','PC2','PC3']].dropna()

model=KMeans(n_clusters=4,random_state=42, n_init=10)
labels=model.fit_predict(cols)

f=open("clusters.txt","w")
f.write("KMeans clustring with k=4\n")
f.write("features: PC1,PC2,PC3\n")

counts = pd.Series(labels).value_counts().sort_index()
for c, n in counts.items():
    f.write("cluster"+str(c)+":"+str(n)+"rows\n")
f.close()

print("Clustering completed and results saved to clusters.txt")