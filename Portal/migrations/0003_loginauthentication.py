# Generated by Django 3.2.7 on 2021-09-14 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0002_address_detail_empid'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginAuthentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='admin', max_length=50)),
                ('userpassword', models.CharField(default='admin', max_length=50)),
                ('role', models.CharField(default='Admin', max_length=50)),
            ],
        ),
    ]
