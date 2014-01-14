from django.conf.urls import include, patterns, url
from django.contrib.auth.views import logout, login

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'curso_adm.views.home', name='home'),

    url(r'^gerencia/', include('curso_adm.gerencia.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Logins
    url(r'^logout/$', logout, {"next_page": "/"}, name="logout"),
    url(r'^signin/$', login, {'template_name': 'login.html'}, name="login"),
)
