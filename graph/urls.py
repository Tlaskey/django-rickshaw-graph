'''
Created on Jul 24, 2014

@author: tlaskey3
'''
from django.conf.urls import url

from graph import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^data$', views.data, name = 'data')
]