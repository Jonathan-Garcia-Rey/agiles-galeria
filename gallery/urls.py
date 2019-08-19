from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_image, name='addImage'),
    url(r'^viewImages', views.viewImages, name='viewImages'),
    url(r'^addNewImage', views.add_new_image, name='addNewImage'),
]
