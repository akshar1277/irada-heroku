from django.contrib import admin
from .models import Non_Technical, Workshop, Seminar, Technical, Event, Fun_Event,Computer,Electrical,Civil,Auto,Chemical,Quiz

class EventAdmin(admin.ModelAdmin):
    list_display=['event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time','platform','rounds','fname','femail','fno','sname','semail','sno']

class Technical_Admin(admin.ModelAdmin):
    list_display=['event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time','platform','rounds','fname','femail','fno','sname','semail','sno']

class Non_Technical_Admin(admin.ModelAdmin):
    list_display=['event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time','platform','rounds','fname','femail','fno','sname','semail','sno']

class Seminar_Admin(admin.ModelAdmin):
   list_display=['event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno']

class Workshop_Admin(admin.ModelAdmin):
    list_display=['event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time','platform','rounds','fname','femail','fno','sname','semail','sno']


class Fun_Event_Admin(admin.ModelAdmin):
   list_display=['event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno']

class Computer_Admin(admin.ModelAdmin):
    list_display=['event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time','platform','rounds','fname','femail','fno','sname','semail','sno']

class Electrical_Admin(admin.ModelAdmin):
    list_display=['event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time','platform','rounds','fname','femail','fno','sname','semail','sno']

class Civil_Admin(admin.ModelAdmin):
   list_display=['event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno']

class Auto_Admin(admin.ModelAdmin):
   list_display=['event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno']

class Chemical_Admin(admin.ModelAdmin):
   list_display=['event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time', 'platform','rounds','fname','femail','fno','sname','semail','sno']

class Quiz_Admin(admin.ModelAdmin):
    list_display=['event_name','image','short_dec','long_dec','rule','overview1','overview2','overview3','fee','participants','date_time','platform','rounds','fname','femail','fno','sname','semail','sno']

# Register your models here.
admin.site.register(Event,EventAdmin)
admin.site.register(Technical,Technical_Admin)
admin.site.register(Non_Technical,Non_Technical_Admin)
admin.site.register(Seminar,Seminar_Admin)
admin.site.register(Workshop,Workshop_Admin)
admin.site.register(Fun_Event,Fun_Event_Admin)
admin.site.register(Computer,Computer_Admin)
admin.site.register(Electrical,Electrical_Admin)
admin.site.register(Civil,Civil_Admin)
admin.site.register(Auto,Auto_Admin)
admin.site.register(Chemical,Chemical_Admin)
admin.site.register(Quiz,Quiz_Admin)
