# Generated by Django 3.2 on 2022-02-08 06:53

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_profile_image',
            field=cloudinary.models.CloudinaryField(default='image/upload/leannes_learners/default_image/bio_placeholder', max_length=255),
        ),
    ]
