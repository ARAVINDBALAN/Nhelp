# Generated by Django 2.1 on 2018-11-22 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happiness', '0012_auto_20181122_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='datelim',
        ),
        migrations.RemoveField(
            model_name='post',
            name='timelim',
        ),
        migrations.AlterField(
            model_name='post',
            name='timelimit',
            field=models.DateTimeField(),
        ),
    ]
