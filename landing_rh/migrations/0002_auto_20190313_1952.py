# Generated by Django 2.1.7 on 2019-03-13 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_rh', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='idade',
        ),
    ]
