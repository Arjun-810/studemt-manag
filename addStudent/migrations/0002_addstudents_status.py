# Generated by Django 3.0.8 on 2020-07-17 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addStudent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addstudents',
            name='status',
            field=models.CharField(default='OK', max_length=200),
        ),
    ]
