import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA


import pandas as pd
# read the csv file

df = pd.read_csv("Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv")
df.head()

df.info()

#Check for missing or null values using df.isna()
df.isnull().sum()

#print type of the flag
print(df['FLAG'].dtype)

# check for unique values
print(df['FLAG'].unique())

# using means to fill in missing values
df['ESTIMATE'] = df['ESTIMATE'].fillna(df['ESTIMATE'].mean())
df['FLAG'] = df['FLAG'].fillna(df['FLAG'].mode())

df.isna().sum()

# check for duplicates in the dataset
df.duplicated().sum()

df.columns

 # Fill numeric columns with mean
numeric_cols = ['UNIT_NUM', 'STUB_NAME_NUM', 'STUB_LABEL_NUM', 'YEAR_NUM', 'AGE_NUM', 'ESTIMATE']
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

 # Fill categorical columns with placeholder
categorical_cols = ['INDICATOR', 'UNIT', 'STUB_NAME', 'STUB_LABEL', 'YEAR', 'AGE', 'FLAG']
for col in categorical_cols:
    df[col] = df[col].fillna("Unknown")

# feature transformation
label_enc = LabelEncoder()

for col in df.select_dtypes(include=['object']).columns:
    df[col] = label_enc.fit_transform(df[col].astype(str))

scaler = StandardScaler()
num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = scaler.fit_transform(df[num_cols])

# Dimensionality Reduction (PCA)
pca = PCA(n_components=3)
df_pca = pca.fit_transform(df[num_cols])

df_pca = pd.DataFrame(df_pca, columns=["PC1", "PC2", "PC3"])

# Discretization
df_pca['PC1_binned'] = pd.cut(df_pca['PC1'], bins=3, labels=[0,1,2])

# Add PCA results to the original DataFrame
df_cleaned = df.copy()

# Add PCA columns
df_cleaned[['PC1', 'PC2', 'PC3']] = df_pca[['PC1', 'PC2', 'PC3']]

# Add binned PC1
df_cleaned['PC1_binned'] = df_pca['PC1_binned']

# Save full dataset
df_cleaned.to_csv("data_preprocessed.csv", index=False)

import os
os.system("python analytics.py data_preprocessed.csv")