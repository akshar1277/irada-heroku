from platform import platform
from django.db import models
from gdstorage.storage import GoogleDriveStorage

from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission
gd_storage = GoogleDriveStorage()

# Create your models here.
class Event(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="event/images", storage=gd_storage)
    short_dec=models.CharField(max_length=200 ,null=True)
    long_dec=models.CharField(max_length=500,null=True)
    rule=models.CharField(max_length=200,null=True)
    overview1=models.CharField(max_length=300,null=True)
    overview2=models.CharField(max_length=300,null=True)
    overview3=models.CharField(max_length=300,null=True)
    fee=models.CharField(max_length=20,null=True)
    participants=models.CharField(max_length=40,null=True)
    date_time=models.DateTimeField()
    platform=models.CharField(max_length=200,null=True)
    rounds=models.IntegerField(null=True)
    fname=models.CharField(max_length=30,null=True)
    femail=models.CharField(max_length=240,null=True)
    fno=models.CharField(max_length=20,null=True)
    sname=models.CharField(max_length=30,null=True)
    semail=models.CharField(max_length=240,null=True)
    sno=models.CharField(max_length=20,null=True)



    def __str__(self):
        return self.event_name

class Technical(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Technical/images", storage=gd_storage)
    short_dec=models.CharField(max_length=200 ,null=True)
    long_dec=models.CharField(max_length=500,null=True)
    rule=models.CharField(max_length=200,null=True)
    overview1=models.CharField(max_length=300,null=True)
    overview2=models.CharField(max_length=300,null=True)
    overview3=models.CharField(max_length=300,null=True)
    fee=models.CharField(max_length=20,null=True)
    participants=models.CharField(max_length=40,null=True)
    date_time=models.DateTimeField()
    platform=models.CharField(max_length=200,null=True)
    rounds=models.IntegerField(null=True)
    fname=models.CharField(max_length=30,null=True)
    femail=models.CharField(max_length=240,null=True)
    fno=models.CharField(max_length=20,null=True)
    sname=models.CharField(max_length=30,null=True)
    semail=models.CharField(max_length=240,null=True)
    sno=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.event_name


class Non_Technical(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Non_Technical/images", storage=gd_storage)
    short_dec=models.CharField(max_length=200 ,null=True)
    long_dec=models.CharField(max_length=500,null=True)
    rule=models.CharField(max_length=200,null=True)
    overview1=models.CharField(max_length=300,null=True)
    overview2=models.CharField(max_length=300,null=True)
    overview3=models.CharField(max_length=300,null=True)
    fee=models.CharField(max_length=20,null=True)
    participants=models.CharField(max_length=40,null=True)
    date_time=models.DateTimeField()
    platform=models.CharField(max_length=200,null=True)
    rounds=models.IntegerField(null=True)
    fname=models.CharField(max_length=30,null=True)
    femail=models.CharField(max_length=240,null=True)
    fno=models.CharField(max_length=20,null=True)
    sname=models.CharField(max_length=30,null=True)
    semail=models.CharField(max_length=240,null=True)
    sno=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.event_name

class Seminar(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Seminar/images" ,storage=gd_storage)
    short_dec=models.CharField(max_length=200 ,null=True)
    long_dec=models.CharField(max_length=500,null=True)
    rule=models.CharField(max_length=200,null=True)
    overview1=models.CharField(max_length=300,null=True)
    overview2=models.CharField(max_length=300,null=True)
    overview3=models.CharField(max_length=300,null=True)
    fee=models.CharField(max_length=20,null=True)
    participants=models.CharField(max_length=40,null=True)
    date_time=models.DateTimeField()
    platform=models.CharField(max_length=200,null=True)
    rounds=models.IntegerField(null=True)
    fname=models.CharField(max_length=30,null=True)
    femail=models.CharField(max_length=240,null=True)
    fno=models.CharField(max_length=20,null=True)
    sname=models.CharField(max_length=30,null=True)
    semail=models.CharField(max_length=240,null=True)
    sno=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.event_name

class Workshop(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Workshop/images" ,storage=gd_storage)
    short_dec=models.CharField(max_length=200 ,null=True)
    long_dec=models.CharField(max_length=500,null=True)
    rule=models.CharField(max_length=200,null=True)
    overview1=models.CharField(max_length=300,null=True)
    overview2=models.CharField(max_length=300,null=True)
    overview3=models.CharField(max_length=300,null=True)
    fee=models.CharField(max_length=20,null=True)
    participants=models.CharField(max_length=40,null=True)
    date_time=models.DateTimeField()
    platform=models.CharField(max_length=200,null=True)
    rounds=models.IntegerField(null=True)
    fname=models.CharField(max_length=30,null=True)
    femail=models.CharField(max_length=240,null=True)
    fno=models.CharField(max_length=20,null=True)
    sname=models.CharField(max_length=30,null=True)
    semail=models.CharField(max_length=240,null=True)
    sno=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.event_name

class Fun_Event(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Fun_Events/images" ,storage=gd_storage)
    short_dec=models.CharField(max_length=200 ,null=True)
    long_dec=models.CharField(max_length=500,null=True)
    rule=models.CharField(max_length=200,null=True)
    overview1=models.CharField(max_length=300,null=True)
    overview2=models.CharField(max_length=300,null=True)
    overview3=models.CharField(max_length=300,null=True)
    fee=models.CharField(max_length=20,null=True)
    participants=models.CharField(max_length=40,null=True)
    date_time=models.DateTimeField()
    platform=models.CharField(max_length=200,null=True)
    rounds=models.IntegerField(null=True)
    fname=models.CharField(max_length=30,null=True)
    femail=models.CharField(max_length=240,null=True)
    fno=models.CharField(max_length=20,null=True)
    sname=models.CharField(max_length=30,null=True)
    semail=models.CharField(max_length=240,null=True)
    sno=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.event_name


#--------------------new ---------------------

class Computer(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Computer/images" ,storage=gd_storage)
    short_dec=models.CharField(max_length=200 ,null=True)
    long_dec=models.CharField(max_length=500,null=True)
    rule=models.CharField(max_length=200,null=True)
    overview1=models.CharField(max_length=300,null=True)
    overview2=models.CharField(max_length=300,null=True)
    overview3=models.CharField(max_length=300,null=True)
    fee=models.CharField(max_length=20,null=True)
    participants=models.CharField(max_length=40,null=True)
    date_time=models.DateTimeField()
    platform=models.CharField(max_length=200,null=True)
    rounds=models.IntegerField(null=True)
    fname=models.CharField(max_length=30,null=True)
    femail=models.CharField(max_length=240,null=True)
    fno=models.CharField(max_length=20,null=True)
    sname=models.CharField(max_length=30,null=True)
    semail=models.CharField(max_length=240,null=True)
    sno=models.CharField(max_length=20,null=True)


    def __str__(self):
        return self.event_name


class Electrical(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Electrical/images",storage=gd_storage)
    short_dec=models.CharField(max_length=200 ,null=True)
    long_dec=models.CharField(max_length=500,null=True)
    rule=models.CharField(max_length=200,null=True)
    overview1=models.CharField(max_length=300,null=True)
    overview2=models.CharField(max_length=300,null=True)
    overview3=models.CharField(max_length=300,null=True)
    fee=models.CharField(max_length=20,null=True)
    participants=models.CharField(max_length=40,null=True)
    date_time=models.DateTimeField()
    platform=models.CharField(max_length=200,null=True)
    rounds=models.IntegerField(null=True)
    fname=models.CharField(max_length=30,null=True)
    femail=models.CharField(max_length=240,null=True)
    fno=models.CharField(max_length=20,null=True)
    sname=models.CharField(max_length=30,null=True)
    semail=models.CharField(max_length=240,null=True)
    sno=models.CharField(max_length=20,null=True)


    def __str__(self):
        return self.event_name

class Civil(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Civil/images",storage=gd_storage)
    short_dec=models.CharField(max_length=200 ,null=True)
    long_dec=models.CharField(max_length=500,null=True)
    rule=models.CharField(max_length=200,null=True)
    overview1=models.CharField(max_length=300,null=True)
    overview2=models.CharField(max_length=300,null=True)
    overview3=models.CharField(max_length=300,null=True)
    fee=models.CharField(max_length=20,null=True)
    participants=models.CharField(max_length=40,null=True)
    date_time=models.DateTimeField()
    platform=models.CharField(max_length=200,null=True)
    rounds=models.IntegerField(null=True)
    fname=models.CharField(max_length=30,null=True)
    femail=models.CharField(max_length=240,null=True)
    fno=models.CharField(max_length=20,null=True)
    sname=models.CharField(max_length=30,null=True)
    semail=models.CharField(max_length=240,null=True)
    sno=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.event_name

class Auto(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Auto/images",storage=gd_storage)
    short_dec=models.CharField(max_length=200 ,null=True)
    long_dec=models.CharField(max_length=500,null=True)
    rule=models.CharField(max_length=200,null=True)
    overview1=models.CharField(max_length=300,null=True)
    overview2=models.CharField(max_length=300,null=True)
    overview3=models.CharField(max_length=300,null=True)
    fee=models.CharField(max_length=20,null=True)
    participants=models.CharField(max_length=40,null=True)
    date_time=models.DateTimeField()
    platform=models.CharField(max_length=200,null=True)
    rounds=models.IntegerField(null=True)
    fname=models.CharField(max_length=30,null=True)
    femail=models.CharField(max_length=240,null=True)
    fno=models.CharField(max_length=20,null=True)
    sname=models.CharField(max_length=30,null=True)
    semail=models.CharField(max_length=240,null=True)
    sno=models.CharField(max_length=20,null=True)


    def __str__(self):
        return self.event_name



class Chemical(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Chemical/images",storage=gd_storage)
    short_dec=models.CharField(max_length=200 ,null=True)
    long_dec=models.CharField(max_length=500,null=True)
    rule=models.CharField(max_length=200,null=True)
    overview1=models.CharField(max_length=300,null=True)
    overview2=models.CharField(max_length=300,null=True)
    overview3=models.CharField(max_length=300,null=True)
    fee=models.CharField(max_length=20,null=True)
    participants=models.CharField(max_length=40,null=True)
    date_time=models.DateTimeField()
    platform=models.CharField(max_length=200,null=True)
    rounds=models.IntegerField(null=True)
    fname=models.CharField(max_length=30,null=True)
    femail=models.CharField(max_length=240,null=True)
    fno=models.CharField(max_length=20,null=True)
    sname=models.CharField(max_length=30,null=True)
    semail=models.CharField(max_length=240,null=True)
    sno=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.event_name

class Quiz(models.Model):
    event_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Quiz/images",storage=gd_storage)
    short_dec=models.CharField(max_length=200 ,null=True)
    long_dec=models.CharField(max_length=500,null=True)
    rule=models.CharField(max_length=200,null=True)
    overview1=models.CharField(max_length=300,null=True)
    overview2=models.CharField(max_length=300,null=True)
    overview3=models.CharField(max_length=300,null=True)
    fee=models.CharField(max_length=20,null=True)
    participants=models.CharField(max_length=40,null=True)
    date_time=models.DateTimeField()
    platform=models.CharField(max_length=200,null=True)
    rounds=models.IntegerField(null=True)
    fname=models.CharField(max_length=30,null=True)
    femail=models.CharField(max_length=240,null=True)
    fno=models.CharField(max_length=20,null=True)
    sname=models.CharField(max_length=30,null=True)
    semail=models.CharField(max_length=240,null=True)
    sno=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.event_name
