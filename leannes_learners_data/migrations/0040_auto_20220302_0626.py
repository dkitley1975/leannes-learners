# Generated by Django 3.2 on 2022-03-02 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0039_auto_20220302_0503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='page_title',
        ),
        migrations.RemoveField(
            model_name='about',
            name='seo_keywords',
        ),
        migrations.RemoveField(
            model_name='about',
            name='seo_page_description',
        ),
    ]