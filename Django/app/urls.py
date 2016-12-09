from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^tabuleiro/$', views.criar_tabuleiro),
	url(r'^tabuleiro/teste/$', views.post_list),
    url(r'^tabuleiro/tabuleiro/$', views.post_tabuleiro),
    url(r'^teste/$', views.post_list),
    url(r'^teste/tabuleiro/$', views.post_tabuleiro),
]
