# Generated by Django 2.1 on 2018-11-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happiness', '0008_user_assisted'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fulfilled',
            field=models.ManyToManyField(blank=True, related_name='fulfilled', to='happiness.post'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='assisted',
        ),
        migrations.AddField(
            model_name='user',
            name='assisted',
            field=models.ManyToManyField(blank=True, related_name='makeassisted', to='happiness.post'),
        ),
    ]
