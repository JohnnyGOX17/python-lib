#!/bin/bash

# map src/ development dir using volumes: https://docs.docker.com/storage/volumes/
dirToMap=/home/jgentile/src
# run Tensorflow GPU supported Docker container image with user's ID and drop into shell, as well as port forward 8888 for Jupyter Lab use on host, and add path for running Jupyter Lab
sudo docker run -p 8888:8888 -v ${dirToMap}:/tf/src -u $(id -u):$(id -g) --gpus all -it tf-gpu-jupyter-lab:latest bash -c 'export PATH=/.local/bin:$PATH; jupyter lab --port=8888 --ip=0.0.0.0 --allow-root --no-browser; bash'
