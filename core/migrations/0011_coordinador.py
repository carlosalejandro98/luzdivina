# Generated by Django 2.1.3 on 2018-12-04 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_agente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCoordinador', models.CharField(max_length=45)),
            ],
        ),
    ]