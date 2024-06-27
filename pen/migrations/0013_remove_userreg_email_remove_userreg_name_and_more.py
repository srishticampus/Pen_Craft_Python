# Generated by Django 5.0.2 on 2024-06-27 17:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pen', '0012_remove_master_lat_remove_master_lon'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userreg',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userreg',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userreg',
            name='phone',
        ),
        migrations.AddField(
            model_name='userreg',
            name='city',
            field=models.CharField(default='Not Provided', max_length=100),
        ),
        migrations.AddField(
            model_name='userreg',
            name='image',
            field=models.ImageField(default='profile/default.jpg', upload_to='Profile'),
        ),
        migrations.AddField(
            model_name='userreg',
            name='location',
            field=models.CharField(default='Not Provided', max_length=100),
        ),
        migrations.AddField(
            model_name='userreg',
            name='phone_number',
            field=models.CharField(default='Not Provided', max_length=20),
        ),
        migrations.AddField(
            model_name='userreg',
            name='qualification',
            field=models.CharField(default='Not Provided', max_length=100),
        ),
        migrations.AddField(
            model_name='userreg',
            name='state',
            field=models.CharField(default='Not Provided', max_length=100),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='address',
            field=models.CharField(default='Not Provided', max_length=255),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
