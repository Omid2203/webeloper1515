# Generated by Django 2.2.5 on 2019-11-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20191108_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='first_day',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='second_day',
            field=models.IntegerField(null=True),
        ),
    ]
