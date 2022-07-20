from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testgame/', include('testgame.urls')),
    path('lobby/', RedirectView.as_view(url='/')),
    path('', include('lobby.urls'))
]
