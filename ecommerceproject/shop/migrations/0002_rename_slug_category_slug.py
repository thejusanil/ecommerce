# Generated by Django 4.1.5 on 2023-02-23 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Slug',
            new_name='slug',
        ),
    ]
