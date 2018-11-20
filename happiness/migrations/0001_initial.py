# Generated by Django 2.1 on 2018-11-17 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import happiness.managers
import places.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff status')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('served', models.IntegerField(blank=True, null=True)),
                ('requested', models.IntegerField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', happiness.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('location', places.fields.PlacesField(max_length=255)),
                ('datesub', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('limit', models.DateTimeField(verbose_name='limit of time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('claims', models.ManyToManyField(blank=True, related_name='getclaims', to=settings.AUTH_USER_MODEL)),
                ('reports', models.ManyToManyField(blank=True, related_name='getreports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
