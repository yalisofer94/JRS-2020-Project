# Generated by Django 3.0.6 on 2020-07-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20200718_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='jrsuser',
            name='company',
            field=models.CharField(default='', max_length=30),
        ),
    ]