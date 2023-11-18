import typer
from sqlmodel import Session
from data.database import engine
from data.models import Turma
from data.models import Aluno
from sqlalchemy.orm import joinedload
from utils.input import TurmaPrompt

app = typer.Typer()

MAPA_TURNOS = {1: "Matutino", 2: "Noturno"}


@app.command()
def listar():
    with Session(engine) as session:
        turmas = session.query(Turma).options(joinedload(Turma.alunos)).all()

    for turma in turmas:
        print(f"ID: {turma.id}")
        print(f"Nome: {turma.nome_turma}")
        print(f"Turno: {MAPA_TURNOS.get(turma.id, 'Turno não encontrado')}")

        if turma.alunos:
            print("Alunos:")
            for aluno in turma.alunos:
                print(f"  - Nome: {aluno.nome}, CPF: {aluno.cpf}, Faixa: {aluno.faixa}")
        else:
            print("Esta turma não possui alunos.")

        print()


if __name__ == "__main__":
    app()
