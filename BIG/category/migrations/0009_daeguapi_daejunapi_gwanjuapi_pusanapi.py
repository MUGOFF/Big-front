# Generated by Django 3.2 on 2022-12-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_seoulapi'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaeguAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds', models.DateField()),
                ('price', models.FloatField(default=0.0)),
                ('ythat', models.FloatField(default=0.0)),
                ('yhat_lower', models.FloatField(default=0.0)),
                ('yhat_upper', models.FloatField(default=0.0)),
                ('item', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DaejunAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds', models.DateField()),
                ('price', models.FloatField(default=0.0)),
                ('ythat', models.FloatField(default=0.0)),
                ('yhat_lower', models.FloatField(default=0.0)),
                ('yhat_upper', models.FloatField(default=0.0)),
                ('item', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GwanjuAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds', models.DateField()),
                ('price', models.FloatField(default=0.0)),
                ('ythat', models.FloatField(default=0.0)),
                ('yhat_lower', models.FloatField(default=0.0)),
                ('yhat_upper', models.FloatField(default=0.0)),
                ('item', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PusanAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds', models.DateField()),
                ('price', models.FloatField(default=0.0)),
                ('ythat', models.FloatField(default=0.0)),
                ('yhat_lower', models.FloatField(default=0.0)),
                ('yhat_upper', models.FloatField(default=0.0)),
                ('item', models.TextField()),
            ],
        ),
    ]
