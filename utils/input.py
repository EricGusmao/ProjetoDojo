from rich.prompt import PromptBase, InvalidResponse
from utils.queries import get_aluno_by_cpf
from validate_docbr import CPF
from rich import print
from typing import List
from sqlmodel import Session
from data.database import engine

TEXTO_TURMA = """
[bold white]1- Manhã[/bold white]\n
[bold bright_yellow]2- Noite[/bold bright_yellow]\n
"""

TEXTO_FAIXA: str = """
[bold white]1- Branca[/bold white]\n
[bold bright_yellow]2- Amarela[/bold bright_yellow]\n
[bold red]3- Vermelha[/bold red]\n
[bold dark_orange]4- Laranja[/bold dark_orange]\n
[bold green]5- Verde[/bold green]\n
[bold purple]6- Roxa[/bold purple]\n
[bold orange4]7- Marrom[/bold orange4]\n
[bold grey42]8- Preta[/bold grey42]
"""


class CpfPrompt(PromptBase[str]):
    response_type = str
    validate_error_message = "[prompt.invalid]Por favor, insira um CPF válido"

    def process_response(self, value: str) -> str:
        value = value.strip()
        if not CPF().validate(value):
            raise InvalidResponse(self.validate_error_message)
        with Session(engine) as session:
            if get_aluno_by_cpf(value, session):
                raise InvalidResponse("[prompt.invalid]Esse CPF já está cadastrado!!!")
        return value

class EditarCpfPrompt(PromptBase[str]):
    response_type = str
    validate_error_message = "[prompt.invalid]Por favor, insira um CPF válido"

    def process_response(self, value: str) -> str:
        value = value.strip()
        if not CPF().validate(value):
            raise InvalidResponse(self.validate_error_message)
        with Session(engine) as session:
            if get_aluno_by_cpf(value, session):
                return value

class IdadePrompt(PromptBase[int]):
    response_type = int
    validate_error_message = "[prompt.invalid]Valor Inválido!!"

    def process_response(self, value: str) -> int:
        value = value.strip()
        try:
            return_value: int = self.response_type(value)
        except ValueError:
            raise InvalidResponse(self.validate_error_message)

        if 5 > return_value >= 100:
            raise InvalidResponse("[prompt.invalid]Idade Inválida!")
        return return_value


class FaixaPrompt(PromptBase[int]):
    response_type = int
    illegal_choice_message = "[prompt.invalid.choice]Opção Não Disponível!!"
    validate_error_message = "[prompt.invalid]Insira um valor válido!!"
    choices: List[str] = ["1", "2", "3", "4", "5", "6", "7", "8"]

    def pre_prompt(self) -> None:
        print(TEXTO_FAIXA)


class TurmaPrompt(PromptBase[int]):
    response_type = int
    illegal_choice_message = "[prompt.invalid.choice]Opção Não Disponível!!"
    validate_error_message = "[prompt.invalid]Insira um valor válido!!"
    choices: List[str] = ["1", "2"]

    def pre_prompt(self) -> None:
        print(TEXTO_TURMA)
