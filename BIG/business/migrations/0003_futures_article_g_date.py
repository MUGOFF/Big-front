# Generated by Django 3.2 on 2022-12-31 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20221231_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='futures_article',
            name='g_date',
            field=models.DateField(default=datetime.datetime(2023, 1, 1, 0, 11, 20, 946216)),
        ),
    ]