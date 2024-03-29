# Generated by Django 4.1.3 on 2022-12-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="School",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, verbose_name="Name")),
                ("created", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sid", models.CharField(max_length=20, verbose_name="Student ID")),
                (
                    "first_name",
                    models.CharField(max_length=20, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=20, verbose_name="Last Name"),
                ),
                ("created", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
