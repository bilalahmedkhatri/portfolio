# Generated by Django 3.2.13 on 2022-07-23 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_api', '0007_auto_20220721_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashedLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hashed_link', models.CharField(max_length=256)),
                ('status', models.BooleanField(default=False)),
                ('clicked', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='freelance_profile',
            field=models.CharField(blank=True, default='gmail.com', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='recommendation',
            field=models.CharField(choices=[('HR', 'Highly Recommanded'), ('RE', 'Recommanded'), ('NR', 'Not Recommanded')], default='RE', max_length=2),
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='social_media',
            field=models.CharField(blank=True, default='gmail.com', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='testimonialmodel',
            name='website',
            field=models.CharField(blank=True, default='gmail.com', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='message',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='testimonialmodel',
            name='message',
            field=models.TextField(max_length=1000),
        ),
    ]
