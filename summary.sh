#!/bin/bash
echo "copying results..."
docker cp bigdata_container:/app/pipeline/data_raw.csv ./results/
docker cp bigdata_container:/app/pipeline/data_preprocessed.csv ./results/
docker cp bigdata_container:/app/pipeline/insight1.txt ./results/
docker cp bigdata_container:/app/pipeline/insight2.txt ./results/
docker cp bigdata_container:/app/pipeline/insight3.txt ./results/
docker cp bigdata_container:/app/pipeline/summary_plot.png ./results/
docker cp bigdata_container:/app/pipeline/clusters.txt ./results/

echo "stopping container..."
docker stop bigdata_container
docker rm bigdata_container
echo "done!"
