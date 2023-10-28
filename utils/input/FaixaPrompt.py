from rich.prompt import PromptBase
from rich import print
from typing import List

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


class FaixaPrompt(PromptBase[int]):
    response_type = int
    illegal_choice_message = "[prompt.invalid.choice]Opção Não Disponível!!"
    validate_error_message = "[prompt.invalid]Insira um valor válido!!"
    choices: List[str] = ["1", "2", "3", "4", "5", "6", "7", "8"]

    def pre_prompt(self) -> None:
        print(TEXTO_FAIXA)
