# Generated by Django 5.1.1 on 2024-10-18 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_tarjama_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarjama',
            name='date',
        ),
    ]