# Generated by Django 3.2.2 on 2021-05-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210517_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='design',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
