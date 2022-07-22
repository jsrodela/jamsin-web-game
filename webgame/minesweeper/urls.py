from django.urls import path

from . import views

app_name = 'minesweeper'
urlpatterns = [
    path('', views.index, name='index'),
]
