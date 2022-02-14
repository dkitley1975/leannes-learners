# Generated by Django 3.2 on 2022-02-08 06:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_userprofile_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='image/upload/leannes_learners/default_image/placeholder', max_length=255),
        ),
    ]