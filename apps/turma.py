import typer
from sqlmodel import Session, select
from rich.table import Table
from rich import print
from data.database import engine
from data.models import Turma

app = typer.Typer()


@app.command()
def listar_alunos():
    # TODO: Mostra uma lista com todos alunos(nome, cpf e faixa) (id da turma como argumento)
    pass


@app.command()
def listar():
    with Session(engine) as session:
        turmas = session.exec(select(Turma)).all()
        tabela = Table(title="Turmas", show_lines=True)
        tabela.add_column("ID", style="cyan")
        tabela.add_column("Nome da Turma", style="magenta")
        tabela.add_column("Qtd de Alunos", style="green")
        for turma in turmas:
            tabela.add_row(f"{turma.id}", f"{turma.nome_turma}", f"{len(turma.alunos)}")
        print(tabela)
