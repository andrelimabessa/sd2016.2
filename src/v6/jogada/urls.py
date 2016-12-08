from django.conf.urls import patterns, url

from jogada import views

urlpatterns = patterns('',  
  url(r'^new$', views.jogada_create, name='jogada_new'),
  url(r'^edit/(?P<pk>\d+)$', views.jogada_update, name='jogada_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.jogada_delete, name='jogada_delete'),  
  url(r'^$', views.jogada_list, name='jogada_list')  
)