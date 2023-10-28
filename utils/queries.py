from data.database import engine
from data.models import Aluno, Turma
from sqlmodel import select, Session


def cpf_ja_existe(cpf: str) -> bool:
    with Session(engine) as session:
        consulta = select(Aluno).where(Aluno.cpf == cpf)
        resultado = session.exec(consulta)
        if resultado.all():
            return True
    return False
