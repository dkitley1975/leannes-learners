# Generated by Django 3.2 on 2022-01-12 10:59

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0021_rename_focus_image_alt_tag_passplus_alt_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=30)),
                ('facebook', models.CharField(blank=True, max_length=80)),
                ('twitter', models.CharField(blank=True, max_length=80)),
            ],
            options={
                'verbose_name': 'Contact/Social Information',
                'verbose_name_plural': 'Contact/Social Information',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TeachingHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=9, unique=True)),
                ('start_time', models.CharField(max_length=6)),
                ('finish_time', models.CharField(blank=True, max_length=6)),
            ],
            options={
                'verbose_name': 'Teaching Hours',
                'verbose_name_plural': 'Teaching Hours',
                'ordering': ['id'],
            },
        ),
    ]
