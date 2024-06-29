# Generated by Django 5.0.2 on 2024-06-29 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pen', '0024_rename_master_check_mark_writingsubmission_spelling_mark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writingsubmission',
            name='grammatical_mark',
        ),
        migrations.RemoveField(
            model_name='writingsubmission',
            name='plagiarism_mark',
        ),
        migrations.RemoveField(
            model_name='writingsubmission',
            name='reviewed_by',
        ),
        migrations.RemoveField(
            model_name='writingsubmission',
            name='spelling_mark',
        ),
        migrations.RemoveField(
            model_name='writingsubmission',
            name='total_mark',
        ),
        migrations.CreateModel(
            name='FeedbackDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spelling_mark', models.IntegerField(default=0)),
                ('plagiarism_mark', models.IntegerField(default=0)),
                ('grammatical_mark', models.IntegerField(default=0)),
                ('master_mark', models.IntegerField(default=0)),
                ('reviewed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pen.writingsubmission')),
            ],
        ),
    ]