#!/bin/bash
echo "copying results..."
docker cp retail_pipeline:/app/pipeline/data_raw.csv ./results/
docker cp retail_pipeline:/app/pipeline/data_preprocessed.csv ./results/
docker cp retail_pipeline:/app/pipeline/insight1.txt ./results/
docker cp retail_pipeline:/app/pipeline/insight2.txt ./results/
docker cp retail_pipeline:/app/pipeline/insight3.txt ./results/
docker cp retail_pipeline:/app/pipeline/summary_plot.png ./results/
docker cp retail_pipeline:/app/pipeline/clusters.txt ./results/

echo "stopping container..."
docker stop retail_pipeline
docker rm retail_pipeline
echo "done!"