# Generated by Django 3.1.1 on 2020-09-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='1234', max_length=300),
        ),
    ]
