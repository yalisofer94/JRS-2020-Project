# Generated by Django 3.0.6 on 2020-07-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20200717_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default='Not specified', max_length=40),
        ),
        migrations.AddField(
            model_name='job',
            name='logo',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
