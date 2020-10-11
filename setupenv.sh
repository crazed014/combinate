#!/bin/sh
apt update
apt upgrade
apt install -y python3-pip python3-flask
export FLASK_APP=combinate.py
export FLASK_ENV=development
pip3 install flask-dropzone
