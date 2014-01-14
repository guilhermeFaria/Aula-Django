# coding: utf-8
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect


from .forms import CursoForm, AlunoCursoForm
from .models import Curso, AlunoCurso

is_superuser = lambda user: user.is_superuser
is_not_superuser = lambda user: not is_superuser()



def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(
        request,
        'gerencia/lista_cursos.html',
        {
            'lista_de_cursos': cursos
        }
    )


def aluno_form(request, pk=None):
    pass


@user_passes_test(is_superuser)
def lista_alunos(request):
    alunos = User.objects.filter(is_superuser=False)
    return render(
        request,
        'gerencia/lista_alunos.html',
        {
            'lista_de_alunos': alunos
        }
    )


@user_passes_test(is_superuser)
def aluno_info(request, pk):
    aluno = get_object_or_404(User, pk=pk)

    aluno_cursos = AlunoCurso.objects.filter(aluno=aluno)

    return render(
        request,
        'gerencia/aluno_cursos.html',
        {
            'aluno_cursos': aluno_cursos,
            'aluno': aluno,
        }
    )
    

@user_passes_test(is_superuser)
def curso_form(request, pk=None):
    if pk:
        curso = get_object_or_404(Curso, pk=pk)
    else:
        curso = Curso()

    form = CursoForm(request.POST or None, instance=curso)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect(reverse('curos_list'))

    return render(
        request,
        'gerencia/curso_form.html',
        {
            'form': form
        }
    )


@user_passes_test(is_superuser)
def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect(reverse('curos_list'))


@user_passes_test(is_superuser)
def lista_matriculas(request):
    matriculas = AlunoCurso.objects.all()
    return render(
        request,
        'gerencia/lista_matriculas.html',
        {
            'lista_de_matriculas': matriculas
        }
    )


# cria uma matricula selecionando Aluno e o curso
@user_passes_test(is_superuser)
def matricula_form(request, aluno_pk=None, curso_pk=None):
    if aluno_pk and curso_pk:
        aluno = get_object_or_404(User, pk=aluno_pk)
        curso = get_object_or_404(Curso, pk=curso_pk)
        alunocurso = get_object_or_404(AlunoCurso, aluno=aluno, curso=curso)
    else:
        aluno = User()
        curso = Curso()
        alunocurso = AlunoCurso()

    form = AlunoCursoForm(request.POST or None, instance=alunocurso)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('/')

    return render(
        request,
        'gerencia/matricula_form.html',
        {
            'aluno': aluno,
            'curso': curso,
            'alunocurso': alunocurso,
            'form': form
        }
    )


# @user_passes_test(is_not_superuser)
# def aluno_matricula_form(request, curso_pk=None):

#     if curso_pk:
#         curso = get_object_or_404(Curso, pk=curso_pk)
#     else:
#         curso = Curso()

#     form = AlunoMatriculaCursoForm(request.POST or None, aluno=request.user, curso=curso)
