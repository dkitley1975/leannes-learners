# Generated by Django 3.2 on 2022-01-13 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0026_auto_20220113_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companydetails',
            name='background_image',
        ),
    ]