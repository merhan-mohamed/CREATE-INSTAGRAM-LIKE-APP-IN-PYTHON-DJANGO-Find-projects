# Generated by Django 2.2.6 on 2020-04-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0004_auto_20200406_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('consumer', 'consumer'), ('staff', 'staff')], max_length=8),
        ),
    ]
