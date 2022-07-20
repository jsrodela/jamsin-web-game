from django.urls import path

from . import views

app_name = 'testgame'
urlpatterns = [
    path('', views.index, name='index'),
]
