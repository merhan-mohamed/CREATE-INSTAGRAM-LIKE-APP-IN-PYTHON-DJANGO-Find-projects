# Generated by Django 2.2.6 on 2020-04-16 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0008_auto_20200411_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetbundle',
            name='base_url',
            field=models.CharField(default='http://s3.amazonaws.com/instacat/', max_length=255),
        ),
    ]