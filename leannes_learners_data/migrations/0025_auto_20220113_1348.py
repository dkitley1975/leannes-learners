# Generated by Django 3.2 on 2022-01-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0024_auto_20220113_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetails',
            name='social_media_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='companydetails',
            name='social_media_name',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
