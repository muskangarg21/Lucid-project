# Generated by Django 2.2.3 on 2019-07-11 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mun_dashboard', '0004_trialmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='type_of_complaint',
        ),
    ]
