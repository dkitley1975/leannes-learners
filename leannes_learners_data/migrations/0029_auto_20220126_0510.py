# Generated by Django 3.2 on 2022-01-26 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0028_terms_and_conditions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Terms_and_Conditions',
            new_name='TermsAndConditions',
        ),
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ['-include_in_carousel', '-slide_identifying_name'], 'verbose_name': 'Home Page Carousel', 'verbose_name_plural': 'Home Page Carousel'},
        ),
    ]