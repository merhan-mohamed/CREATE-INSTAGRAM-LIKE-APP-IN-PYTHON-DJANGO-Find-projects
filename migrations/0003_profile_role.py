# Generated by Django 2.2.6 on 2020-04-06 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0002_item_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('consumer', 'consumer'), ('staff', 'staff')], default=1, max_length=8),
            preserve_default=False,
        ),
    ]
