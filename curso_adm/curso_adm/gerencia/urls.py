from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    # Curso
    url(r'^curso/list/$', 'curso_adm.gerencia.views.lista_cursos', name='curso_list'),
    url(r'^curso/form/$', 'curso_adm.gerencia.views.curso_form', name='curso_form'),
    url(r'^curso/form/(?P<pk>\d+)/$', 'curso_adm.gerencia.views.curso_form', name='curso_form'),
    url(r'^curso/delete/(?P<pk>\d+)/$', 'curso_adm.gerencia.views.curso_delete', name='curso_delete'),

    # Aluno
    url(r'^aluno/list/$', 'curso_adm.gerencia.views.lista_alunos', name='aluno_list'),
    url(r'^aluno/form/$', 'curso_adm.gerencia.views.aluno_form', name='aluno_form'),
    url(r'^aluno/form/(?P<pk>\d+)/$', 'curso_adm.gerencia.views.aluno_form', name='aluno_form'),
    # url(r'^aluno/delete/(?P<pk>\d+)/$', 'curso_adm.gerencia.views.aluno_delete', name='aluno_delete'),

    # Matricula
    url(r'^matricula/list/$', 'curso_adm.gerencia.views.lista_matriculas', name='matricula_list'),
    url(r'^matricula/form/$', 'curso_adm.gerencia.views.matricula_form', name='matricula_form'),
    url(r'^matricula/form/aluno:(?P<aluno_pk>\d+)/curso:(?P<curso_pk>\d+)/$', 'curso_adm.gerencia.views.matricula_form', name='matricula_form'),
    # url(r'^matricula/delete/(?P<pk>\d+)/$', 'curso_adm.gerencia.views.matricula_delete', name='matricula_delete')
)
