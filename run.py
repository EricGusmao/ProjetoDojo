import typer
from apps import turma, aluno
from data.database import create_db_and_tables

app = typer.Typer()
app.add_typer(turma.app, name="turma")
app.add_typer(aluno.app, name="aluno")
if __name__ == "__main__":
    create_db_and_tables()
    app()
