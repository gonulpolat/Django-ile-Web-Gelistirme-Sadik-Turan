# Generated by Django 4.1.3 on 2024-07-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Courses", "0008_remove_course_category_course_categories"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="isHome",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="course",
            name="isActive",
            field=models.BooleanField(default=False),
        ),
    ]
