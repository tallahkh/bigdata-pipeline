# 📊 Suicide Death Rates — Big Data Pipeline
**CSCI461: Introduction to Big Data — Assignment #1 | Spring 2026**

## Team Members
- Member 1: Lina Ashraf Sediq
- Member 2: Tallah Khaled Kamal

---

## 📁 Project Structure
```
bigdataproject/
├── Dockerfile
├── ingest.py
├── preprocess.py
├── analytics.py
├── visualize.py
├── cluster.py
├── summary.sh
├── README.md
└── results/
    ├── data_raw.csv
    ├── data_preprocessed.csv
    ├── insight1.txt
    ├── insight2.txt
    ├── insight3.txt
    ├── summary_plot.png
    └── clusters.txt
```

---

## 🐳 Docker Commands

### 1. Build the image
```bash
docker build -t suicide-pipeline.
```

### 2. Run the container
```bash
docker run -it --name suicide_pipeline suicide-pipeline
```

### 3. Run the pipeline inside the container
```bash
python ingest.py "Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv"
```

### 4. Copy results to host and cleanup
```bash
bash summary.sh
```

---

## 🔄 Execution Flow
```
ingest.py → preprocess.py → analytics.py → visualize.py → cluster.py
```

| Script | Input | Output |
|---|---|---|
| `ingest.py` | dataset CSV | data_raw.csv |
| `preprocess.py` | data_raw.csv | data_preprocessed.csv |
| `analytics.py` | data_preprocessed.csv | insight1.txt, insight2.txt, insight3.txt |
| `visualize.py` | data_preprocessed.csv | summary_plot.png |
| `cluster.py` | data_preprocessed.csv | clusters.txt |

---

## 🧹 Preprocessing Steps

- **Data Cleaning:** filled missing ESTIMATE with mean, filled missing FLAG with Unknown, removed duplicates
- **Feature Transformation:** encoded all categorical columns with LabelEncoder, scaled all numeric columns with StandardScaler
- **Dimensionality Reduction:** applied PCA and kept 3 components (PC1, PC2, PC3)
- **Discretization:** binned PC1 into 3 categories (low, mid, high)

---

## 📊 Dataset
**Death Rates for Suicide by Sex, Race, Hispanic Origin, and Age — United States**
- Source: CDC / National Center for Health Statistics
- Rows: 6,390
- Columns: 13
