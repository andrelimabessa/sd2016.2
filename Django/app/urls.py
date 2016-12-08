from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^teste/$', views.post_list),
    url(r'^teste/tabuleiro/$', views.post_tabuleiro),
]