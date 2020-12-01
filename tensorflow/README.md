## Tensorflow in Docker Container w/GPU Support

1. Install NVIDIA proprietary driver first, _see Additional Drivers in Ubuntu, or [download install file](https://www.nvidia.com/Download/index.aspx?lang=en-us)_
2. [Install Docker](https://docs.docker.com/engine/install/)
3. [Setup NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installing-on-ubuntu-and-debian)
  - Test to make sure `$ sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi` completes correctly with the correct GPU SMI output.
4. `$ sudo docker pull tensorflow/tensorflow:latest-gpu-jupyter` to download the [latest Tensorflow Docker image](https://www.tensorflow.org/install/docker) w/GPU support and Jupyter notebooks
  - Test Tensorflow container(s) with `$ sudo docker run --gpus all -it --rm tensorflow/tensorflow:latest-gpu \
   python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`
5. Run the Docker container and drop into a bash shell (with your user ID) as `$ sudo docker run -u $(id -u):$(id -g) --gpus all -it tensorflow/tensorflow:latest-gpu-jupyter bash`

