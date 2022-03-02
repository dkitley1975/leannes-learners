# Generated by Django 3.2 on 2022-03-02 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0037_auto_20220131_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='seo_keywords',
            field=models.CharField(default='1', max_length=160, verbose_name='Page Keywords - seperate by a ,'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='seo_page_description',
            field=models.CharField(default='1', max_length=160, verbose_name='Page Description - Googles preview'),
            preserve_default=False,
        ),
    ]
