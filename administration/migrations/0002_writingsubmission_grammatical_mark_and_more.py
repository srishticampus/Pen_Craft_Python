# Generated by Django 4.2.4 on 2024-06-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='writingsubmission',
            name='grammatical_mark',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='writingsubmission',
            name='master_check_mark',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='writingsubmission',
            name='plagiarism_mark',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='writingsubmission',
            name='reviewed_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='writingsubmission',
            name='total_mark',
            field=models.IntegerField(default=0),
        ),
    ]
