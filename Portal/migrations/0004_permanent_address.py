# Generated by Django 3.2.7 on 2021-09-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0003_loginauthentication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permanent_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_type', models.CharField(default='permanent address', max_length=30)),
                ('empid', models.CharField(max_length=30)),
                ('add_id', models.CharField(max_length=30)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('dist', models.CharField(max_length=100)),
                ('state', models.CharField(default='uppp', max_length=100)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
    ]
