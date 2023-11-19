import typer
from rich import print
from rich.table import Table
from sqlmodel import Session
from data.database import engine
from data.models import Aluno, TypeFaixa
from utils.input import (
    CpfPrompt,
    IdadePrompt,
    FaixaPrompt,
    TurmaPrompt,
)
from rich.prompt import Prompt, Confirm
from utils.input import get_aluno_by_cpf

app = typer.Typer()

CPF_NAO_ENCONTRADO: str = "[bold red]CPF não encontrado! :( [/bold red]"


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
        print("[bold green]Aluno cadastrado com sucesso ;)[/bold green]")


@app.command()
def buscar(cpf: str):
    with Session(engine) as session:
        aluno = get_aluno_by_cpf(cpf, session)
        if not aluno:
            return print(CPF_NAO_ENCONTRADO)
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
    with Session(engine) as session:
        aluno = get_aluno_by_cpf(cpf, session)
        if not aluno:
            return print(CPF_NAO_ENCONTRADO)

        print("[bold]Campos disponíveis para edição:[/bold]")
        print("1. Nome")
        print("2. Idade")
        print("3. Faixa")
        print("4. Turma")

        campo_a_editar = Prompt.ask("Informe qual campo que deseja editar: ")

        match campo_a_editar:
            case "1":
                aluno.nome = Prompt.ask("Nome completo", default=aluno.nome)
            case "2":
                aluno.idade = IdadePrompt.ask("Idade", default=aluno.idade)
            case "3":
                aluno.faixa = TypeFaixa(
                    FaixaPrompt.ask(
                        "Faixa", default=TypeFaixa(aluno.faixa), show_choices=False
                    )
                )
            case "4":
                aluno.turma_id = TurmaPrompt.ask(
                    "Turma", default=aluno.turma_id, show_choices=False
                )
            case _:
                return print("[bold red]Opção inválida! [/bold red]")

        confirmacao = Confirm.ask("Deseja aplicar as alterações?")
        if confirmacao:
            session.add(aluno)
            session.commit()
            print("[bold green]Aluno editado com sucesso! :)[/bold green]")
        else:
            print("[bold yellow]Edição cancelada.[/bold yellow]")


@app.command()
def excluir(cpf: str):
    with Session(engine) as session:
        aluno = get_aluno_by_cpf(cpf, session)
        if not aluno:
            return print(CPF_NAO_ENCONTRADO)

        confirmacao = Confirm.ask(
            f"Tem certeza que deseja excluir o aluno {aluno.nome}?"
        )
        if not confirmacao:
            return print(
                f"[bold red]Operação para deletar o aluno {aluno.nome} foi cancelada![/bold red]"
            )

        session.delete(aluno)
        session.commit()
        print(f"[bold yellow]Aluno {aluno.nome} foi deletado![/bold yellow]")
