# Generated by Django 2.1 on 2018-11-24 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happiness', '0016_auto_20181124_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(blank=True, default='phone', max_length=20),
            preserve_default=False,
        ),
    ]
