# Generated by Django 3.2 on 2022-01-02 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0004_testimonials'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testimonials',
            new_name='Testimonial',
        ),
    ]
