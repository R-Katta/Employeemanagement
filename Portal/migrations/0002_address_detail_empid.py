# Generated by Django 3.2.7 on 2021-09-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address_detail',
            name='empid',
            field=models.CharField(default='empid', max_length=30),
        ),
    ]
