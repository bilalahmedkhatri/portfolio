#!/bin/bash

echo "installing libraries..."

pip install -r requirements.txt

echo "packages installed."

echo "<======= CREATE DATABASE ======>"

python manage.py makemigrations
python manage.py migrate

echo "<(------ CREATE SUPER USER ------)>"

python manage.py createsuperuser

echo "<(------ CREATING STATIC DIRECTORY ------)>"

python manage.py collectstatic

sudo apt install -y ufw

echo "<([===== START DJANGO SERVER ON '0.0.0.0:8000' =====])>"

python manage.py runserver 0.0.0.0:8000