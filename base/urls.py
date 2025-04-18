from django.urls import path
from .views import *

urlpatterns = [
   path('index/',index),
   path('contact/',contact_us),
   path('home/',home),
   path('task/',list),
   path('task/create/',create),
   path('task/<pk>',mark),
   path('task/<pk>/edit/', edit)
]
