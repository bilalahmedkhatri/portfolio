#!/bin/bash
echo " <<======= linux packages updating ========>> "

apt update && apt-get update && apt upgrade -y


echo " {{===== Install python 3.11, python3-pip CURL, GIT =====}} "

apt install -y python3.11 python3-pip curl git postgresql postgresql-contrib && apt update -y

echo " {{===== Starting POSTGRESQL SERVER =====}} "

systemctl restart postgresql.service

echo "installing libraries..."

pip install -r requirements.txt

echo "required packages installed."

echo "<======= CREATE DATABASE ======>"

python3 manage.py makemigrations

python3 manage.py migrate

echo "<(------ CREATE SUPER USER ------)>"

python3 manage.py createsuperuser

echo "<(------ CREATING STATIC DIRECTORY ------)>"

python3 manage.py collectstatic

sudo apt install -y ufw

echo "<([===== START DJANGO SERVER ON '0.0.0.0:8000' =====])>"

python3 manage.py runserver 0.0.0.0:8000