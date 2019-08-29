from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views


urlpatterns = [
    
    url('^$',views.index, name = 'index'),
    url(r'^date/$',views.date,name='bank'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
   
]