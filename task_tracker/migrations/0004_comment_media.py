# Generated by Django 5.1.1 on 2024-11-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='comments_media'),
        ),
    ]