from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import EventSerializer, Non_Technical_Serializer,Technical_Serializer, Workshop_Serializer,Seminar_Serializer,Fun_Event_Serializer,Computer_Serializer,Electrical_Serializer,Civil_Serializer,Auto_Serializer,Chemical_Serializer,Quiz_Serializer
from .models import Non_Technical, Workshop, Seminar, Technical, Event, Fun_Event,Computer,Electrical,Civil,Auto,Chemical,Quiz
# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all().order_by('-id')
    serializer_class=EventSerializer

class Technical_ViewSet(viewsets.ModelViewSet):
    queryset=Technical.objects.all().order_by('-id')
    serializer_class=Technical_Serializer

class Non_Technical_ViewSet(viewsets.ModelViewSet):
    queryset=Non_Technical.objects.all().order_by('-id')
    serializer_class=Non_Technical_Serializer

class  Workshop_ViewSet(viewsets.ModelViewSet):
    queryset=Workshop.objects.all().order_by('-id')
    serializer_class=Workshop_Serializer

class Seminar_ViewSet(viewsets.ModelViewSet):
    queryset=Seminar.objects.all().order_by('-id')
    serializer_class=Seminar_Serializer

class Fun_Event_ViewSet(viewsets.ModelViewSet):
    queryset=Fun_Event.objects.all().order_by('-id')
    serializer_class=Fun_Event_Serializer

class Computer_ViewSet(viewsets.ModelViewSet):
    queryset=Computer.objects.all().order_by('-id')
    serializer_class=Computer_Serializer

class Electrical_ViewSet(viewsets.ModelViewSet):
    queryset=Electrical.objects.all().order_by('-id')
    serializer_class=Electrical_Serializer

class Civil_ViewSet(viewsets.ModelViewSet):
    queryset=Civil.objects.all().order_by('-id')
    serializer_class=Civil_Serializer

class Auto_ViewSet(viewsets.ModelViewSet):
    queryset=Auto.objects.all().order_by('-id')
    serializer_class=Auto_Serializer

class Chemical_ViewSet(viewsets.ModelViewSet):
    queryset=Chemical.objects.all().order_by('-id')
    serializer_class=Chemical_Serializer

class Quiz_ViewSet(viewsets.ModelViewSet):
    queryset=Quiz.objects.all().order_by('-id')
    serializer_class=Quiz_Serializer
