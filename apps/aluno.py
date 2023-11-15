import typer
from rich import print
from rich.table import Table
from sqlmodel import Session
from data.database import engine
from data.models import Aluno, TypeFaixa
from utils.input import (
    CpfPrompt,
    EditarCpfPrompt,
    IdadePrompt,
    FaixaPrompt,
    TurmaPrompt,
)
from rich.prompt import Prompt, Confirm
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
        tabela.add_row("Turma", f"{aluno.turma.nome_turma}") # TODO: Verificar se turma é None
    print(tabela)


@app.command()
def editar(cpf: str):
    with Session(engine) as session:
        aluno = get_aluno_by_cpf(cpf, session)
        if not aluno:
            return print("[bold red]CPF não encontrado! :( [/bold red]")

        print("[bold]Campos disponíveis para edição:[/bold]")
        print("1. Nome")
        print("2. Idade")
        print("3. Faixa")
        print("4. Turma")

        campo_a_editar = Prompt.ask("Informe qual campo que deseja editar: ")

        if campo_a_editar == "1":
            aluno.nome = Prompt.ask("Nome completo", default=aluno.nome)
        elif campo_a_editar == "2":
            aluno.idade = IdadePrompt.ask("Idade", default=aluno.idade)
        elif campo_a_editar == "3":
            aluno.faixa = TypeFaixa(
                FaixaPrompt.ask(
                    "Faixa", default=TypeFaixa(aluno.faixa).name, show_choices=False
                )
            )
        elif campo_a_editar == "4":
            aluno.turma_id = TurmaPrompt.ask(
                "Turma", default=aluno.turma.nome_turma, show_choices=False
            )
        else:
            return print("[bold red]Opção inválida! [/bold red]")

        confirmacao = Confirm.ask("Deseja aplicar as alterações?")
        if confirmacao:
            session.add(aluno)
            session.commit()
            print("[bold green]Aluno editado com sucesso! :)[/bold green]")
        else:
            print("[bold yellow]Edição cancelada.[/bold yellow]")


@app.command()
def excluir():
    with Session(engine) as session:
        alunos = session.query(Aluno).all()
        if not alunos:
            return print("[bold red]Não há alunos cadastrados! :( [/bold red]")

        print("[bold]Alunos disponíveis para exclusão:[/bold]")
        for i, aluno in enumerate(alunos, start=1):
            print(f"{i}. {aluno.nome} (CPF: {aluno.cpf})")

        opcao = Prompt.ask("Informe o número do aluno que deseja excluir")

        try:
            opcao = int(opcao)
            if 1 <= opcao <= len(alunos):
                exclusao = alunos[opcao - 1]
                confirmacao = Confirm.ask(
                    f"Tem certeza que deseja deletar o aluno {exclusao.nome}?"
                )
                if confirmacao:
                    session.delete(exclusao)
                    session.commit()
                    print(
                        f"[bold yellow]Aluno {exclusao.nome} foi deletado![/bold yellow]"
                    )
                else:
                    print(
                        f"[bold red]Operação para deletar o aluno {exclusao.nome} foi cancelada![/bold red]"
                    )
            else:
                print("[bold red]Opção inválida![/bold red]")
        except ValueError:
            print("[bold red]Informe um número válido![/bold red]")
