# Generated by Django 3.2 on 2022-03-03 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0044_auto_20220303_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='passplus',
            name='seo_description',
            field=models.CharField(default='1', max_length=150, verbose_name='Google search description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passplus',
            name='seo_title',
            field=models.CharField(default='', max_length=50, unique=True, verbose_name='Page tab title'),
            preserve_default=False,
        ),
    ]
