# Generated by Django 3.0.7 on 2020-12-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_auto_20201220_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=177444, unique=True),
        ),
    ]