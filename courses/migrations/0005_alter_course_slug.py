# Generated by Django 4.1.3 on 2023-07-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_slug_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
