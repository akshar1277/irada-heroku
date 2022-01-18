from rest_framework import serializers
from .models import Non_Technical, Workshop, Seminar,Technical, Event, Fun_Event,Chemical,Computer,Electrical,Civil,Auto,Quiz



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=('id','event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno')


class Non_Technical_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Non_Technical
        fields=('id','event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno')


class Technical_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Technical
        fields=('id','event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno')


class Workshop_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Workshop
        fields=('id','event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno')


class Seminar_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Seminar
        fields=('id','event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno')


class Fun_Event_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Fun_Event
        fields=('id','event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno')

class Computer_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Computer
        fields=('id','event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno')

class Electrical_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Electrical
        fields=('id','event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno')

class Civil_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Civil
        fields=('id','event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno')

class Auto_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Auto
        fields=('id','event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno')

class Chemical_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Chemical
        fields=('id','event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno')


class Quiz_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=('id','event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno')
