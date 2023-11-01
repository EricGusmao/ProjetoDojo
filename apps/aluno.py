import typer
from rich import print
from rich.table import Table
from sqlmodel import Session
from data.database import engine
from data.models import Aluno, TypeFaixa
from utils.input import CpfPrompt, IdadePrompt, FaixaPrompt, TurmaPrompt
from rich.prompt import Prompt
from utils.input import get_aluno_by_cpf

app = typer.Typer()


@app.command()
def cadastrar():
    nome = Prompt.ask("Nome completo")
    idade = IdadePrompt.ask("Idade")
    cpf = CpfPrompt.ask("CPF")
    faixa = FaixaPrompt.ask("Faixa", show_choices=False)
    turma_id = TurmaPrompt.ask("Turma", show_choices=False)

    novo_aluno = Aluno(
        nome=nome, turma_id=turma_id, cpf=cpf, faixa=TypeFaixa(faixa), idade=idade
    )
    with Session(engine) as session:
        session.add(novo_aluno)
        session.commit()


@app.command()
def buscar(cpf: str):
    with Session(engine) as session:
        aluno = get_aluno_by_cpf(cpf, session)
        if not aluno:
            return print("[bold red]CPF não encontrado! :( [/bold red]")
        tabela = Table(show_header=False)
        tabela.add_column("", style="magenta")
        tabela.add_column("", style="cyan")
        tabela.add_row("Nome", f"{aluno.nome}")
        tabela.add_row("Idade", f"{aluno.idade}")
        tabela.add_row("CPF", f"{aluno.cpf}")
        tabela.add_row("Faixa", f"{TypeFaixa(aluno.faixa).name}")
        tabela.add_row("Turma", f"{aluno.turma.nome_turma}")
    print(tabela)


@app.command()
def editar(cpf: str):
    pass


@app.command()
def excluir(cpf: str):
    pass
