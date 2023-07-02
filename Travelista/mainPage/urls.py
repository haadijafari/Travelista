from django.urls import path
from mainPage.views import *

urlpatterns = [
    path('', mainPage, name='Travelista'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
