# Generated by Django 3.2 on 2021-04-21 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safevote_app', '0008_auto_20210420_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='IV',
            field=models.BinaryField(max_length=128),
        ),
        migrations.AlterField(
            model_name='block',
            name='key',
            field=models.BinaryField(max_length=128),
        ),
    ]