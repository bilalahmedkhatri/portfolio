#!/bin/bash

# This script sets up and runs a Django portfolio project

# Update system packages
echo " <<======= linux packages updating ========>> "
apt update && apt-get update && apt upgrade -y

# Install required system dependencies
echo " {{===== Install python 3.11, python3-pip, python3-venv, CURL, postgresql, GIT =====}} "
apt install -y python3.11 python3-pip python3-venv curl git postgresql postgresql-contrib && apt update -y

# Install Python package management tools
echo "installing libraries..."
pip3 install pipenv
pipenv shell 

# Start PostgreSQL database server
echo " {{===== Starting POSTGRESQL SERVER =====}} "
service postgresql start

echo "required packages installed."

# Install Python dependencies from requirements file
pip install -r requirements.txt

# Set up Django database
echo "<======= CREATE DATABASE ======>"
python3 manage.py makemigrations
python3 manage.py migrate

# Create Django superuser for admin access
echo "<(------ CREATE SUPER USER ------)>"
python3 manage.py createsuperuser

# Collect static files for Django
echo "<(------ CREATING STATIC DIRECTORY ------)>"
python3 manage.py collectstatic

# Install UFW (Uncomplicated Firewall)
sudo apt install -y ufw

# Start Django development server
echo "<([===== START DJANGO SERVER ON '0.0.0.0:8000' =====])>"
python3 manage.py runserver 0.0.0.0:8000
