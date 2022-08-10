from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('minesweeper/', include('minesweeper.urls')),
    path('omok/', include('omok.urls')),
    path('lobby/', RedirectView.as_view(url='/')),
    path('', include('lobby.urls'))
]
