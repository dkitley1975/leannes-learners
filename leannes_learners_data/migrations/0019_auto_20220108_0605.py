# Generated by Django 3.2 on 2022-01-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0018_remove_passplus_background_image_alt_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passplus',
            old_name='content',
            new_name='lead_content',
        ),
        migrations.AddField(
            model_name='passplus',
            name='main_content',
            field=models.TextField(default='text'),
            preserve_default=False,
        ),
    ]
