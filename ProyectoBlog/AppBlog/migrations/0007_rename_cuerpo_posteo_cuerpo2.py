# Generated by Django 4.1.3 on 2023-01-21 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0006_alter_posteo_cuerpo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posteo',
            old_name='cuerpo',
            new_name='cuerpo2',
        ),
    ]