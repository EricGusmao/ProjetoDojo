import typer
from rich import print
from sqlmodel import Session
from data.database import engine
from data.models import Aluno, TypeFaixa
from utils.input import CpfPrompt, IdadePrompt, FaixaPrompt, TurmaPrompt
from rich.prompt import Prompt
from utils.input import get_aluno_by_cpf

app = typer.Typer()


@app.command()
def cadastrar():
    nome = Prompt.ask("Nome completo:")
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
    aluno = get_aluno_by_cpf(cpf)
    if not aluno:
        return print("[bold red]CPF não encontrado! :( [/bold red]")


@app.command()
def editar(cpf: str):
    aluno = get_aluno_by_cpf(cpf)
    if not aluno:
        return print("[bold red]CPF não encontrado! :( [/bold red]")


@app.command()
def excluir():
    # TODO: Exclui aluno, pede confirmacao antes de excluir
    pass
