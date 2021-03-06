# Generated by Django 3.2 on 2022-02-15 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20220215_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='blog.comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(verbose_name='Eye Catching Excerpt -make someone want to read the article'),
        ),
    ]
