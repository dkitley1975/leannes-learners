# Generated by Django 3.2 on 2022-01-13 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0023_auto_20220113_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companydetails',
            old_name='social_media_link_1',
            new_name='social_media_name',
        ),
        migrations.RemoveField(
            model_name='companydetails',
            name='social_media_name_1',
        ),
    ]
