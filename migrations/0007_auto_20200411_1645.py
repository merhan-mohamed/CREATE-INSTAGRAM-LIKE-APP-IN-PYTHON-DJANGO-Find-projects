# Generated by Django 2.2.6 on 2020-04-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0006_auto_20200407_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('consumer', 'consumer'), ('staff', 'staff')], max_length=8),
        ),
    ]