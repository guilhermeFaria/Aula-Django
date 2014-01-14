from django import forms
from django.contrib.auth.models import User

from .models import Curso, AlunoCurso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso


class AlunoCursoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super (AlunoCursoForm, self).__init__(*args, **kwargs)
        self.fields['aluno'].queryset = User.objects.exclude(is_superuser=True)

    class Meta:
        model = AlunoCurso
