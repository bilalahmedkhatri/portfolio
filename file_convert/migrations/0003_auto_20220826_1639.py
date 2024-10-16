# Generated by Django 3.2.13 on 2022-08-26 11:39

from django.db import migrations, models
import file_convert.models


class Migration(migrations.Migration):

    dependencies = [
        ('file_convert', '0002_convertfile_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='convertfile',
            name='converted_file_dir',
            field=models.FileField(blank=True, null=True, upload_to=file_convert.models.ConvertFile.converted_file),
        ),
        migrations.AddField(
            model_name='convertfile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
