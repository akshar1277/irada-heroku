# Generated by Django 3.2.9 on 2021-12-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20211231_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='rounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='chemical',
            name='rounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='civil',
            name='rounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='rounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='electrical',
            name='rounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='rounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fun_event',
            name='rounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='non_technical',
            name='rounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='rounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='rounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='technical',
            name='rounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='rounds',
            field=models.IntegerField(null=True),
        ),
    ]
