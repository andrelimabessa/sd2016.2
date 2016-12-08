from django.conf.urls import include, url

from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/jogo/', include('jogo.urls', namespace='jogo')),
    url(r'^app/jogo/(?P<jogoId>\d+)/jogada/', include('jogada.urls', namespace='jogada')),
    url(r'^app/jogada/', include('jogada.urls', namespace='jogada')),    
    url(r'^$', 'apps.views.start'),
    url(r'^app/$', 'apps.views.home'),
    url(r'^app/sair$', 'apps.views.sair'),
]
