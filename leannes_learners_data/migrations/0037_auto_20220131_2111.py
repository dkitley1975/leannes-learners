# Generated by Django 3.2 on 2022-01-31 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0036_auto_20220128_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_us',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='passplus',
            name='lead_content',
            field=models.TextField(verbose_name='Lead content - more prominent than the rest.'),
        ),
        migrations.AlterField(
            model_name='passplus',
            name='main_content',
            field=models.TextField(verbose_name='Main content of the page.'),
        ),
        migrations.AlterField(
            model_name='terms',
            name='lead_content',
            field=models.TextField(verbose_name='Lead content - The explanation.'),
        ),
        migrations.AlterField(
            model_name='terms',
            name='main_content',
            field=models.TextField(verbose_name='The Terms and Conditions.'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial',
            field=models.TextField(),
        ),
    ]