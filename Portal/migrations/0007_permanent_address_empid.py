# Generated by Django 3.2.7 on 2021-09-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0006_remove_permanent_address_empid'),
    ]

    operations = [
        migrations.AddField(
            model_name='permanent_address',
            name='empid',
            field=models.CharField(default='empid', max_length=30),
        ),
    ]
