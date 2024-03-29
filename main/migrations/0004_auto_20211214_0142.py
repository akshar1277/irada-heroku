# Generated by Django 3.2.9 on 2021-12-13 20:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_event_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AU_ME',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='', upload_to='AU_ME/images')),
                ('short_dec', models.CharField(max_length=200)),
                ('long_dec', models.CharField(max_length=500)),
                ('rule', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('venue', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Civil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='', upload_to='Civil/images')),
                ('short_dec', models.CharField(max_length=200)),
                ('long_dec', models.CharField(max_length=500)),
                ('rule', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('venue', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CS_IT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='', upload_to='CS_IT/images')),
                ('short_dec', models.CharField(max_length=200)),
                ('long_dec', models.CharField(max_length=500)),
                ('rule', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('venue', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ele_Ec_Ic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='', upload_to='Ele_Ec_Ic/images')),
                ('short_dec', models.CharField(max_length=200)),
                ('long_dec', models.CharField(max_length=500)),
                ('rule', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('venue', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fun_Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='', upload_to='Fun_Events/images')),
                ('short_dec', models.CharField(max_length=200)),
                ('long_dec', models.CharField(max_length=500)),
                ('rule', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('venue', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 20, 12, 22, 419604, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
