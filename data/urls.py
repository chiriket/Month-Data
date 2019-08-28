from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views


urlpatterns = [
    
    url('^$',views.index, name = 'index'),
    url(r'^date/$',views.bank,name='bank'),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',
        views.MerchDescription.as_view()),
    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'^accounts/', include('registration.backends.simple.urls')),
   
]