# Generated by Django 2.2.28 on 2022-08-12 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_devtest123"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="devtest123",
            name="name",
        ),
        migrations.AddField(
            model_name="devtest123",
            name="name23",
            field=models.TextField(blank=True),
        ),
    ]
