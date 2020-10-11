#!/bin/sh
apt update
apt upgrade -y
apt install -y python3-pip python3-flask
pip3 install flask-dropzone



