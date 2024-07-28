# Generated by Django 4.1.3 on 2024-07-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Courses", "0009_course_ishome_alter_course_isactive"),
    ]

    operations = [
        migrations.CreateModel(
            name="Upload",
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
                ("image", models.ImageField(upload_to="images")),
            ],
        ),
        migrations.AlterField(
            model_name="course",
            name="imageUrl",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="course",
            name="title",
            field=models.CharField(max_length=50),
        ),
    ]