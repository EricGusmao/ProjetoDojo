import typer
from sqlmodel import Session, select
from rich.table import Table
from rich import print
from data.database import engine
from data.models import Turma, TypeFaixa
from utils.queries import get_turma_by_id

app = typer.Typer()


@app.command("listar-alunos")
def listar_alunos(id: int):
    with Session(engine) as session:
        turma = get_turma_by_id(id, session)
        if not turma:
            return print("[bold red]Turma não encontrada! :( [/bold red]")
        alunos = turma.alunos
        if len(alunos) <= 0:
            return print("[bold red]Não há alunos nessa turma :( [/bold red]")
        tabela = Table(title=f"{turma.nome_turma}", show_lines=True)
        tabela.add_column("CPF", style="cyan")
        tabela.add_column("Nome", style="magenta")
        tabela.add_column("Faixa", style="green")
        for aluno in alunos:
            tabela.add_row(
                f"{aluno.cpf}", f"{aluno.nome}", f"{TypeFaixa(aluno.faixa).name}"
            )
        print(tabela)


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
