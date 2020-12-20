# Generated by Django 3.0.7 on 2020-12-20 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academica', '0002_auto_20201220_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clase',
            name='nivel',
        ),
        migrations.RemoveField(
            model_name='clase_profesor',
            name='clase',
        ),
        migrations.RemoveField(
            model_name='clase_profesor',
            name='profesor',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='clase',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='periodo',
        ),
        migrations.RemoveField(
            model_name='perfil_profesor',
            name='nivel',
        ),
        migrations.RemoveField(
            model_name='perfil_profesor',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='Clase',
        ),
        migrations.DeleteModel(
            name='Clase_Profesor',
        ),
        migrations.DeleteModel(
            name='Nota',
        ),
        migrations.DeleteModel(
            name='Perfil_Profesor',
        ),
        migrations.DeleteModel(
            name='Periodo',
        ),
    ]