# Generated by Django 5.0.1 on 2024-01-19 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Books",
            new_name="Book",
        ),
    ]