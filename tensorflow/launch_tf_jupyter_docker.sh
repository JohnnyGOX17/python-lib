#!/bin/bash

sudo docker run -u $(id -u):$(id -g) --gpus all -it tensorflow/tensorflow:latest-gpu-jupyter bash
