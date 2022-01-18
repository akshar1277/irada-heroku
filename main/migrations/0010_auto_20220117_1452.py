# Generated by Django 3.2.9 on 2022-01-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20211231_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='chemical',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='civil',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='electrical',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='event',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='fun_event',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='non_technical',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='seminar',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='technical',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='venue',
        ),
        migrations.AddField(
            model_name='auto',
            name='fee',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='femail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='fno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='overview1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='overview2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='overview3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='participants',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='platform',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='semail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='sname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='sno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='fee',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='femail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='fno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='overview1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='overview2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='overview3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='participants',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='platform',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='semail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='sname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='sno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='fee',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='femail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='fno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='overview1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='overview2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='overview3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='participants',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='platform',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='semail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='sname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='civil',
            name='sno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='fee',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='femail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='fno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='overview1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='overview2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='overview3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='participants',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='platform',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='semail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='sname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='sno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='electrical',
            name='fee',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='electrical',
            name='femail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='electrical',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='electrical',
            name='fno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='electrical',
            name='overview1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='electrical',
            name='overview2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='electrical',
            name='overview3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='electrical',
            name='participants',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='electrical',
            name='platform',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='electrical',
            name='semail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='electrical',
            name='sname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='electrical',
            name='sno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='fee',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='femail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='fno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='overview1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='overview2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='overview3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='platform',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='semail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='sname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='sno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fun_event',
            name='fee',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fun_event',
            name='femail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='fun_event',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='fun_event',
            name='fno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='fun_event',
            name='overview1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='fun_event',
            name='overview2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='fun_event',
            name='overview3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='fun_event',
            name='participants',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fun_event',
            name='platform',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fun_event',
            name='semail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='fun_event',
            name='sname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='fun_event',
            name='sno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='non_technical',
            name='fee',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='non_technical',
            name='femail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='non_technical',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='non_technical',
            name='fno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='non_technical',
            name='overview1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='non_technical',
            name='overview2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='non_technical',
            name='overview3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='non_technical',
            name='participants',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='non_technical',
            name='platform',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='non_technical',
            name='semail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='non_technical',
            name='sname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='non_technical',
            name='sno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='fee',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='femail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='fno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='overview1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='overview2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='overview3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='participants',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='platform',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='semail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='sname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='sno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='fee',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='femail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='fno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='overview1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='overview2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='overview3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='participants',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='platform',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='semail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='sname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='sno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='technical',
            name='fee',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='technical',
            name='femail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='technical',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='technical',
            name='fno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='technical',
            name='overview1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='technical',
            name='overview2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='technical',
            name='overview3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='technical',
            name='participants',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='technical',
            name='platform',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='technical',
            name='semail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='technical',
            name='sname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='technical',
            name='sno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='fee',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='femail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='fno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='overview1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='overview2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='overview3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='participants',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='platform',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='semail',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='sname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='sno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='auto',
            name='long_dec',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='auto',
            name='rule',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='auto',
            name='short_dec',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='chemical',
            name='long_dec',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='chemical',
            name='rule',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='chemical',
            name='short_dec',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='civil',
            name='long_dec',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='civil',
            name='rule',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='civil',
            name='short_dec',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='long_dec',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='rule',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='short_dec',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='electrical',
            name='long_dec',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='electrical',
            name='rule',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='electrical',
            name='short_dec',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='long_dec',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='rule',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_dec',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fun_event',
            name='long_dec',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='fun_event',
            name='rule',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fun_event',
            name='short_dec',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='non_technical',
            name='long_dec',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='non_technical',
            name='rule',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='non_technical',
            name='short_dec',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='long_dec',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='rule',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='short_dec',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='long_dec',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='rule',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='short_dec',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='technical',
            name='long_dec',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='technical',
            name='rule',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='technical',
            name='short_dec',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='long_dec',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='rule',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='short_dec',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
