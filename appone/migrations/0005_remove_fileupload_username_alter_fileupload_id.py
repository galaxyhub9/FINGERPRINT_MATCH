# Generated by Django 4.1.3 on 2022-11-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0004_fileupload_username_alter_fileupload_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='username',
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
