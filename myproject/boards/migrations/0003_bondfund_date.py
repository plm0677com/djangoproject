# Generated by Django 3.0.5 on 2020-12-11 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_bondfund'),
    ]

    operations = [
        migrations.AddField(
            model_name='bondfund',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
