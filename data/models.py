from enum import IntEnum
from typing import List, Optional
from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel, Enum, Column

class TypeFaixa(IntEnum):
    branca = 1
    amarela = 2
    vermelha = 3
    laranja = 4
    verde = 5
    roxa = 6
    marrom = 7
    preta = 8


class Turma(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    nome_turma: str
    alunos: List["Aluno"] = Relationship(back_populates="turma")


class Aluno(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("cpf"),)
    id: Optional[int] = Field(primary_key=True, default=None)
    nome: str
    idade: int
    cpf: str
    faixa: TypeFaixa = Field(sa_column=Column(Enum(TypeFaixa)), nullable=False)
    turma_id: int = Field(foreign_key="turma.id", nullable=False)
    turma: Turma = Relationship(back_populates="alunos")
