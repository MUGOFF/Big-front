# Generated by Django 3.2 on 2022-12-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20221209_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='writer',
            field=models.CharField(default='익명', max_length=250),
        ),
    ]
