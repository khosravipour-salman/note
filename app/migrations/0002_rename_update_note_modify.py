# Generated by Django 3.2 on 2022-04-28 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='update',
            new_name='modify',
        ),
    ]