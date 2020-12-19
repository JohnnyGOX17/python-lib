#!/bin/bash

echo "Launched Docker instances:"
sudo docker ps -a
echo "Restart last container created..."
sudo docker start $(sudo docker ps -q -l)
echo "Reattach terminal & stdin"
sudo docker attach $(sudo docker ps -q -l)

