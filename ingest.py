# ingest.py
import sys
import pandas as pd
import os

# get the path of the dataset

if len(sys.argv) < 2:
    print("Usage: python ingest.py <dataset_file_path>")
    sys.exit(1)

input_file = sys.argv[1]

 
# check if the file exists
 
if not os.path.exists(input_file):
    print(f"Error: File '{input_file}' does not exist.")
    sys.exit(1)

# load the dataset
# Some raw datasets may require latin1 encoding
try:
    df = pd.read_csv(input_file, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(input_file, encoding='latin1')

 
# save the raw copy

df.to_csv("data_raw.csv", index=False)
print("Dataset ingested successfully! Saved as data_raw.csv")
 
# Call preprocess.py automatically

os.system("python preprocess.py data_raw.csv")
