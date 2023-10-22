import typer
import turmas, alunos

app = typer.Typer()
app.add_typer(turmas.app, name="turmas")
app.add_typer(alunos.app, name="alunos")
if __name__ == "__main__":
    app()
