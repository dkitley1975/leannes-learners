# Generated by Django 3.2 on 2022-01-07 12:23

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0013_delete_pupilstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pass_plus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('background_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255)),
                ('background_image_alt_tag', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('focus_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255)),
                ('focus_image_alt_tag', models.CharField(blank=True, max_length=200)),
                ('updated_at', models.DateField(auto_now=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
