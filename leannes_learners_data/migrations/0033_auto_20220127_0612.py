# Generated by Django 3.2 on 2022-01-27 06:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0032_auto_20220127_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_us',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='slide_text_description',
            field=tinymce.models.HTMLField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='passplus',
            name='main_content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='terms',
            name='lead_content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='terms',
            name='main_content',
            field=tinymce.models.HTMLField(),
        ),
    ]
