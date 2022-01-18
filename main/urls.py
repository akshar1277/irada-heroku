from django.urls import path,include
from rest_framework import routers, urlpatterns
from .views import EventViewSet,Technical_ViewSet,Non_Technical_ViewSet,Seminar_ViewSet,Workshop_ViewSet,Fun_Event_ViewSet,Computer_ViewSet,Electrical_ViewSet,Civil_ViewSet,Auto_ViewSet,Chemical_ViewSet,Quiz_ViewSet


router=routers.DefaultRouter()
router.register(r'Event',EventViewSet)
router.register(r'Technical',Technical_ViewSet)
router.register(r'Non_Technical',Non_Technical_ViewSet)
router.register(r'Workshop',Workshop_ViewSet)
router.register(r'Seminar',Seminar_ViewSet)
router.register(r'Fun_Events',Fun_Event_ViewSet)
router.register(r'Computer',Computer_ViewSet)
router.register(r'Electrical',Electrical_ViewSet)
router.register(r'Civil',Civil_ViewSet)
router.register(r'Auto',Auto_ViewSet)
router.register(r'Chemical',Chemical_ViewSet)
router.register(r'Quiz',Quiz_ViewSet)




urlpatterns = [
    path('',include(router.urls)),
]



