# Generated by Django 3.2 on 2022-01-28 16:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220128_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Eye Catching Excerpt - make someone want to read the article'),
        ),
    ]