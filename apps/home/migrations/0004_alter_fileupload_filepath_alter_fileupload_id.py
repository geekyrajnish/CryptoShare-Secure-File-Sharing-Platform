# Generated by Django 4.0.1 on 2022-01-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_fileupload_filepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='filepath',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
