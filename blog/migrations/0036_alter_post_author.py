# Generated by Django 3.2 on 2022-03-05 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0035_auto_20220304_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='post_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
