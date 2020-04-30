from django.urls import path

from . import views
from .views import *

urlpatterns = [
    #path('', views.index, name = 'index'),
    #path('', views.hello, name = 'hello'),
    path('', regform, name = 'registration form'),
    path('add', views.add, name = 'add')
]