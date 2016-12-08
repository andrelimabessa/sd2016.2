from django.conf.urls import patterns, url

from jogo import views
from jogada import views as views_jogada

urlpatterns = patterns('',
  url(r'^$', views.jogo_list, name='jogo_list'),
  url(r'^new$', views.jogo_create, name='jogo_new'),
  url(r'^edit/(?P<pk>\d+)$', views.jogo_update, name='jogo_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.jogo_delete, name='jogo_delete'),  
  #url(r'../jogada$', views.jogo_jogadas, name='jogo_jogadas'),
  url(r'^(?P<pk>\d+)/jogada$', views.jogo_jogadas, name='jogo_jogadas'),
)