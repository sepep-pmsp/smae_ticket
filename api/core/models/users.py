from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional

from .database import Base
from .estrutura_administrativa import Orgao
from .tickets import Ticket

#evitando import circular
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .estrutura_administrativa import Orgao
    from .chamado import Chamado

from .cross_tables import user_perfil, perfil_permissao


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email : Mapped[str] = mapped_column(unique=True)
    nome : Mapped[str]
    hashed_password : Mapped[str]
    is_ativo : Mapped[bool]
    
    orgao_id: Mapped[int] = mapped_column(ForeignKey("orgaos.id"))
    orgao: Mapped[Orgao] = relationship(back_populates="usuarios")
    perfis: Mapped[List["Perfil"]] = relationship(secondary=user_perfil, back_populates='users')
    chamados : Mapped[Optional[List["Chamado"]]] = relationship()

class Perfil(Base):
    __tablename__ = "perfis"

    id: Mapped[int] = mapped_column(primary_key=True)
    title :  Mapped[str] = mapped_column()
    description : Mapped[str] = mapped_column()

    permissoes: Mapped[List["Permissao"]] = relationship(secondary=perfil_permissao)
    users: Mapped[Optional[List["User"]]] = relationship(secondary=user_perfil, back_populates='perfis')


class Permissao(Base):
    __tablename__ = "permissoes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)