# Generated by Django 3.2 on 2022-03-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0040_auto_20220302_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='featured_order',
            field=models.IntegerField(default='1', verbose_name='Featured Price Order results display 1,3,2'),
            preserve_default=False,
        ),
    ]
