from data.database import engine
from data.models import Aluno, Turma
from sqlmodel import select, Session
from sqlalchemy.exc import NoResultFound
from typing import List


def get_aluno_by_cpf(cpf: str, session: Session) -> Aluno | None:
    try:
        aluno = session.exec(select(Aluno).where(Aluno.cpf == cpf)).one()
    except NoResultFound:
        return None
    else:
        return aluno


def get_turma_by_id(id: int, session: Session) -> Turma | None:
    try:
        turma = session.exec(select(Turma).where(Turma.id == id)).one()
    except NoResultFound:
        return None
    else:
        return turma
