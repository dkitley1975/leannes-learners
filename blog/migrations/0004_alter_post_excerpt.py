# Generated by Django 3.2 on 2022-01-28 17:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Eye Catching Excerpt - make someone want to read the article'),
        ),
    ]