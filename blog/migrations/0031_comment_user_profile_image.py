# Generated by Django 3.2 on 2022-03-01 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_user_bio'),
        ('blog', '0030_alter_post_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_profile_image',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to='users.userprofile'),
            preserve_default=False,
        ),
    ]
