# Generated by Django 3.2 on 2022-12-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_rename_potato_carrot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gwanju',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField()),
                ('ds', models.DateField()),
                ('ythat', models.FloatField(default=0.0)),
                ('yhat_lower', models.FloatField(default=0.0)),
                ('yhat_upper', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Seoul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds', models.DateField()),
                ('ythat', models.FloatField(default=0.0)),
                ('yhat_lower', models.FloatField(default=0.0)),
                ('yhat_upper', models.FloatField(default=0.0)),
                ('item', models.TextField()),
            ],
        ),
    ]