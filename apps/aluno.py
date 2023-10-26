import typer
from sqlmodel import Session
from data.database import engine
from data.models import Aluno

app = typer.Typer()


@app.command()
def cadastrar():
    # TODO: Realiza o cadastro
    # PRECISA DE VALIDACAO!!!!!!
    pass


@app.command()
def buscar():
    # TODO: Busca aluno por cpf (argumento) e mostra os detalhes
    pass


@app.command()
def sem_turma():
    # TODO: Mostra todos os alunos que estao sem turma
    # (o output e parecido com o comando turma mostrar_alunos)
    pass


@app.command()
def editar():
    # TODO: Edita dados do aluno (cpf como argumento)
    # PRECISA DE VALIDACAO!!!!!!
    pass


@app.command()
def excluir():
    # TODO: Exclui aluno, pede confirmacao antes de excluir
    pass
