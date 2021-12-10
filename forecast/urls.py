from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='test'),
    path('predict', views.prediction, name='predict'),

]
