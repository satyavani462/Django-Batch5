# Generated by Django 3.0.8 on 2020-09-02 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_auto_20200902_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='Name',
            field=models.CharField(help_text='Enter Your Full Name', max_length=30),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='Phone',
            field=models.CharField(help_text='Enter you 10 digit mobile number', max_length=10),
        ),
        migrations.AlterModelTable(
            name='faculty',
            table='siri_data',
        ),
    ]