# Generated by Django 3.0.7 on 2020-12-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20200419_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=805058, unique=True),
        ),
    ]
