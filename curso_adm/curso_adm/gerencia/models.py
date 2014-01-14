from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    nome = models.CharField(max_length=180, null=True, blank=False)

    def __unicode__(self):
        return self.nome or u''


class AlunoCurso(models.Model):
    curso = models.ForeignKey(Curso)
    aluno = models.ForeignKey(User)
    data = models.DateField(auto_now_add=True)


    def __unicode__(self):
        return u'%s: %s' % (self.aluno, self.curso)
