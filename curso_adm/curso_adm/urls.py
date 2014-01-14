from django.conf.urls import include, patterns, url
from django.contrib.auth.views import logout, login

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'curso_adm.views.home', name='home'),

    url(r'^gerencia/', include('curso_adm.gerencia.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^perfil/$', 'znc_contatos.core.views.perfil_form', name="perfil_form"),

    # Logins
    url(r'^logout/$', logout, {"next_page": "/"}, name="logout"),
    url(r'^signin/$', login, {'template_name': 'login.html'}, name="login"),
    # url(r'^signup/$', 'znc_contatos.core.views.signup', name="signup"),

    # password Reset
    url(
        r'^user/password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect': '/user/password/reset/done/'},
        name="password_reset"
    ),
    url(
        r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'
    ),
    url(
        r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect': '/user/password/done/'}
    ),
    url(
        r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'
    ),
)
