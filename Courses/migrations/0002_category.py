# Generated by Django 4.1.3 on 2024-07-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Courses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50)),
                ("slug", models.CharField(max_length=50)),
            ],
        ),
    ]