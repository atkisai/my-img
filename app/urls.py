from django.conf.urls import url
from blog import views

from app import views

urlpatterns=[

    url(r'^index',views.index, name='index'),
    url(r'^images',views.images, name='images'),

]