# Generated by Django 4.1.3 on 2022-11-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0008_fileupload_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='username',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
