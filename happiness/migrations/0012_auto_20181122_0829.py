# Generated by Django 2.1 on 2018-11-22 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happiness', '0011_user_reported'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datelim',
            field=models.DateField(default='2018-11-11'),
        ),
        migrations.AddField(
            model_name='post',
            name='timelim',
            field=models.TimeField(default='08:28:02'),
        ),
        migrations.AlterField(
            model_name='post',
            name='timelimit',
            field=models.DateTimeField(blank=True),
        ),
    ]
