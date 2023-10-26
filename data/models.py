from typing import List, Optional
from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel


class Turma(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    nome_turma: str
    turno: str  # [matutino, vespertino ou noturno] TODO: validar
    alunos: List["Aluno"] = Relationship(back_populates="turma")


class Aluno(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("cpf"),)
    id: Optional[int] = Field(primary_key=True, default=None)
    nome: str
    idade: int
    cpf: str
    faixa: str  # [branca, amarela, vermelha, laranja, verde, roxa, marrom, preta] TODO: validar
    turma_id: Optional[int] = Field(foreign_key="turma.id", default=None)
    turma: Optional[Turma] = Relationship(back_populates="alunos")
