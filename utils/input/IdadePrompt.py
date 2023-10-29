from rich.prompt import PromptBase, InvalidResponse


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
