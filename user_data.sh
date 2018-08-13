#!/bin/bash
sudo apt-get update -y
sudo apt-get install -y python3 python3-pip python3-dev build-essential
sudo apt-get install -y git
git clone https://github.com/danielSbastos/dale-slack-tf.git
cd dale-slack-tf
pip install -r requirements.txt
python app.py
