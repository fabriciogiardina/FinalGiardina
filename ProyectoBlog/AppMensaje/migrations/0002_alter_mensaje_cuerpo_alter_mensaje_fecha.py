# Generated by Django 4.1.3 on 2023-01-22 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMensaje', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='cuerpo',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='fecha',
            field=models.DateField(),
        ),
    ]
