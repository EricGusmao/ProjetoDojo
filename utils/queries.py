from data.database import engine
from data.models import Aluno, Turma
from sqlmodel import select, Session
from sqlalchemy.exc import NoResultFound


def get_aluno_by_cpf(cpf: str) -> Aluno | bool:
    with Session(engine) as session:
        try:
            aluno = session.exec(select(Aluno).where(Aluno.cpf == cpf)).one()
        except NoResultFound:
            return False
        else:
            return aluno
