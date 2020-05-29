#!/bin/bash
sudo apt-get update
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
sudo apt-get update
sudo apt-get -y install docker-ce docker-ce-cli containerd.io
mkdir volume
sudo mount /dev/vdc volume/
sudo docker run -d -p 8888:8888 -p 6006:6006 -e "PASSWORD=password" -v ~/volume:/notebooks/ALL_NOTEBOOKS --name jupyter --restart always sglanger/jupyter_with_keras
