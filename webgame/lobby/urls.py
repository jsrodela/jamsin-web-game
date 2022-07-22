from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'lobby'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='lobby/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    # path('', include('django.contrib.auth.urls')),
]
