# Generated by Django 3.0.7 on 2020-12-20 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20201214_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=7664, unique=True),
        ),
    ]
