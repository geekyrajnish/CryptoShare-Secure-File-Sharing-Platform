# Generated by Django 4.0.1 on 2022-01-28 21:28

import apps.home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_fileupload_delete_priyanshu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='filepath',
            field=models.FileField(null=True, upload_to=apps.home.models.path_and_rename),
        ),
    ]