# Generated by Django 5.0.7 on 2024-12-23 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_author_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='Article_no',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='author',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='author',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default='..@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='author',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
