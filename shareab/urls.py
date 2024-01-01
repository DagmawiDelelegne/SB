from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
   
    path('', views.home, name= ""),

    path('register', views.register, name = "register"),

    path('login', views.my_login, name='login'),

    path('logout', views.my_logout, name="logout"),

    path('dashboard', views.dashboard, name="dashboard"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)