# Generated by Django 3.2 on 2022-01-07 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leannes_learners_data', '0015_alter_pass_plus_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_at'], 'verbose_name': 'Blog Post', 'verbose_name_plural': 'Blog Posts'},
        ),
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ['-include_in_carousel', '-slide_identifying_name'], 'verbose_name': 'Home Page Carousel content', 'verbose_name_plural': 'Home Page Carousel content'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at'], 'verbose_name': 'Blog Post Comment', 'verbose_name_plural': 'Blog Post Comments'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-featured', 'service_duration'], 'verbose_name': 'Service Description', 'verbose_name_plural': 'Service Descriptions'},
        ),
        migrations.AlterModelOptions(
            name='testimonial',
            options={'ordering': ['-created_at'], 'verbose_name': 'Testimonial', 'verbose_name_plural': 'Testimonials'},
        ),
    ]
