import typer
from apps import turma, aluno
from data.models import Turma
from data.database import create_db_and_tables, engine
from sqlmodel import Session, select


def gerar_alunos():
    with open("tests/pessoas.json", "r") as pessoas_file:
        pessoas = json.load(pessoas_file)
    with Session(engine) as session:
        for pessoa in pessoas:
            novo_aluno = Aluno(
                nome=pessoa["nome"],
                faixa=pessoa["faixa"],
                idade=pessoa["idade"],
                cpf=pessoa["cpf"],
                turma_id=pessoa["turma_id"],
            )
            session.add(novo_aluno)
        session.commit()


def criar_turmas():
    with Session(engine) as session:
        turmas = session.exec(select(Turma)).all()
        if not turmas:
            turma1 = Turma(nome_turma="Matutino")
            turma2 = Turma(nome_turma="Noturno")
            session.add(turma1)
            session.add(turma2)
            session.commit()


app = typer.Typer()
app.add_typer(turma.app, name="turma")
app.add_typer(aluno.app, name="aluno")
if __name__ == "__main__":
    create_db_and_tables()
    criar_turmas()
    app()
