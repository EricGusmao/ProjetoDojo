import typer
from sqlmodel import Session
from data.database import engine
from data.models import Turma

app = typer.Typer()


@app.command()
def listar_alunos():
    # TODO: Mostra uma lista com todos alunos(nome, cpf e faixa) (id da turma como argumento)
    pass
