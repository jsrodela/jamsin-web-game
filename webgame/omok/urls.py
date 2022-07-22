from django.urls import path

from . import views

app_name = 'omok'
urlpatterns = [
    path('', views.index, name='index'),
]
