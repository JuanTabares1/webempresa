# Generated by Django 5.1.5 on 2025-01-17 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['name'], 'verbose_name': 'enlace', 'verbose_name_plural': 'enlaces'},
        ),
    ]
