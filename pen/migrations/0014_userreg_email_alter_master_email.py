# Generated by Django 5.0.2 on 2024-06-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pen', '0013_remove_userreg_email_remove_userreg_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreg',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='master',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
