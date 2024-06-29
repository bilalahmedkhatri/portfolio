from dataclasses import dataclass
from distutils.util import change_root
from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.forms import CharField
from django.utils.crypto import get_random_string


class ContactFormModel(models.Model):
    full_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(max_length=1000)

    # auto update fields
    date_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.full_name


class TestimonialModel(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    website = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(max_length=1000)
    social_media = models.CharField(max_length=256, null=True, blank=True)
    freelance_profile = models.CharField(max_length=256, null=True, blank=True)
    RECOMMANDATION = (
        ('HR', 'Highly Recommanded'),
        ("RE", "Recommanded"),
        ("NR", "Not Recommanded"),
    )
    recommendation = models.CharField(
        max_length=2, choices=RECOMMANDATION, default="RE")
    status = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)

    def file_upload_add(instance, file_upload):
        date_time = datetime.now()
        char = get_random_string(length=10)
        file_extension = file_upload.split('.')[1]
        file_upload = f"{date_time.day}_{char}.{file_extension}"
        path_formated = f"{date_time.year}/{date_time.month}/"
        path = "image/" + path_formated + file_upload
        return path

    test_image_02 = models.ImageField(
        upload_to=file_upload_add, blank=True, null=True)

    def __str__(self):
        return self.full_name


class HashedLink(models.Model):
    Hashed_link = models.CharField(max_length=256)
    status = models.BooleanField(default=False)
    clicked = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date_time
    

class ProjectsModel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    refrence = models.CharField(max_length=100, blank=True, null=True)
    STATUS = (
        ('PS', 'Posted'),
        ("PN", "Pending"),
    )
    status = models.CharField(
        max_length=2, choices=STATUS, default="RE")
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def file_upload_add(instance, file_upload):
        date_time = datetime.now()
        char = get_random_string(length=10)
        file_extension = file_upload.split('.')[1]
        file_upload = f"{date_time.day}_{char}.{file_extension}"
        path_formated = f"{date_time.year}/{date_time.month}/"
        path = path_formated + file_upload
        return path

    image = models.ImageField(
        upload_to=file_upload_add, blank=True, null=True)

    def __str__(self):
        return self.title
