from rich.prompt import PromptBase, InvalidResponse
from utils.queries import cpf_ja_existe
from validate_docbr import CPF


class CpfPrompt(PromptBase[str]):
    response_type = str
    validate_error_message = "[prompt.invalid]Por favor, insira um CPF válido"

    def process_response(self, value: str) -> str:
        value = value.strip()
        validador = CPF()
        if not validador.validate(value):
            raise InvalidResponse(self.validate_error_message)
        if cpf_ja_existe(value):
            raise InvalidResponse("[prompt.invalid]Esse CPF já está cadastrado!!!")
        return value
