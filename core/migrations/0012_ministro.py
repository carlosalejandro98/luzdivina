# Generated by Django 2.1.3 on 2018-12-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_coordinador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ministro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMinistro', models.CharField(max_length=45)),
            ],
        ),
    ]