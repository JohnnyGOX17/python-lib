## Tensorflow in Docker Container w/GPU Support

1. Install NVIDIA proprietary driver first, _see Additional Drivers in Ubuntu, or [download install file](https://www.nvidia.com/Download/index.aspx?lang=en-us)_
2. [Install Docker](https://docs.docker.com/engine/install/)
3. [Setup NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installing-on-ubuntu-and-debian)
  - Test to make sure `$ sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi` completes correctly with the correct GPU SMI output.
4. `$ sudo docker pull tensorflow/tensorflow:latest-gpu-jupyter` to download the [latest Tensorflow Docker image](https://www.tensorflow.org/install/docker) w/GPU support and Jupyter notebooks
  - Test Tensorflow container(s) with `$ sudo docker run --gpus all -it --rm tensorflow/tensorflow:latest-gpu \
   python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`
5. Run `sudo docker run -p 8888:8888 -u $(id -u):$(id -g) --gpus all -it tensorflow/tensorflow:latest-gpu-jupyter bash` to start Docker container and drop into shell.
6. Install any other packages like [SciPy](https://www.scipy.org/install.html) or [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) in Docker shell.
7. Run Jupyter Notebook using `jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root --no-browser .` or Jupyter Lab with `jupyter lab --port=8888 --ip=0.0.0.0 --allow-root --no-browser`.
8. `exit` out of Docker container and find launched container ID with `docker ps -a`
9. Save container changes to new image `docker commit <CONTAINER_ID> [NEW_IMAGE_NAME]`, it will now show in `docker images`.
10. Either reattach to container (see below commands) or run `launch_tf_jupyter_docker.sh` to start new Docker container and drop into shell.

### Other Docker commands

* Restart last container created: `docker start $(docker ps -q -l)`
  + Reattach terminal & stdin to last: `docker attach $(docker ps -q -l)`
* List currently running Docker instances: `docker ps -a`
* Stop all containers: `docker kill $(docker ps -q)`
* Remove all containers: `docker rm $(docker ps -a -q)`
* Remove all docker images: `docker rmi $(docker images -q)`

