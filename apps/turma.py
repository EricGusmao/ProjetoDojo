import typer
from sqlmodel import Session
from data.database import engine
from data.models import Turma

app = typer.Typer()


@app.command()
def criar():
    # TODO: Usuario cria uma turma
    pass


@app.command()
def listar():
    # TODO: Imprime o nome da turma, id e turno como se fosse numa tabela
    pass


@app.command()
def mostrar_alunos():
    # TODO: Mostra uma lista com todos alunos(nome, cpf e faixa) (id da turma como argumento)
    pass


@app.command()
def editar():
    # TODO: Edita a turma
    pass


@app.command()
def excluir():
    # TODO: Exclui a turma
    # TESTAR O QUE ACONTECE COM OS ALUNOS QUANDO SE DELETA UMA TURMA
    pass
