import imp
from django.contrib import admin
from django.apps import apps


for model in apps.get_app_config('file_convert').get_models():
    admin.site.register(model)