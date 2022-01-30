# Generated by Django 3.2 on 2022-01-26 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0030_rename_termsandconditions_terms'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ['-include_in_carousel', '-slide_identifying_name'], 'verbose_name': 'Carousel on Home Page', 'verbose_name_plural': 'Carousel on Home Page'},
        ),
        migrations.AlterModelOptions(
            name='passplus',
            options={'ordering': ['-created_at'], 'verbose_name': 'Pass Plus Page', 'verbose_name_plural': 'Pass Plus Page'},
        ),
        migrations.AlterModelOptions(
            name='terms',
            options={'ordering': ['-created_at'], 'verbose_name': 'Terms and Conditions Page', 'verbose_name_plural': 'Terms and Conditions Page'},
        ),
    ]