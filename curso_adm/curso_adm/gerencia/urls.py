from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^curso/list/$', 'curso_adm.gerencia.views.lista_cursos', name='curos_list'),
    url(r'^curso/form/$', 'curso_adm.gerencia.views.curso_form', name='curos_form'),
    url(r'^curso/form/(?P<pk>\d+)/$', 'curso_adm.gerencia.views.curso_form', name='curos_form'),
)
