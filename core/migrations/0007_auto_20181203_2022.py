# Generated by Django 2.1.3 on 2018-12-03 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_comunidadcatolica'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comunidadcatolica',
            old_name='nombreComunidad',
            new_name='NombreComunidad',
        ),
    ]
