# Generated by Django 3.0.8 on 2020-07-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addStudent', '0003_addstudents_roll_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='addstudents',
            name='message',
            field=models.CharField(default='none', max_length=500),
        ),
    ]
