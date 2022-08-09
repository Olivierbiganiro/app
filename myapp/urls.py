
from unicodedata import name
from django.urls import path
from  django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from djangoProject3 import settings
from . import views
from django.contrib.auth.models import User
urlpatterns = [

    path('home', views.home, name='home'),
    path('logout', views.logoutsite, name='logout'),
    path('database', views.datab_data, name='datab_data'),
    path('signin', views.signin, name='signin'),
    path('profile', views.profiledata, name='profile'),
    path('register', views.register, name='register'),
    path('contact', views.contactdata, name='cont'),
    path('newprofile', views.profile2, name='newprofile'),
    path('edit/', views.edit, name='edit'),
    path('sametest',views.test),
    path('play',views.play, name='play')
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)