# Generated by Django 3.0.8 on 2020-07-17 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addStudent', '0002_addstudents_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='addstudents',
            name='Roll_no',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]