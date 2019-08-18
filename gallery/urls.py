from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
