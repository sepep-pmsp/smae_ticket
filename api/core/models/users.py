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

user_perfil = Table(
    "user_perfil",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("perfil_id", ForeignKey("perfis.id")),
)


perfil_permissao = Table(
    "perfil_permissao",
    Base.metadata,
    Column("perfil_id", ForeignKey("perfis.id")),
    Column("permissao_id", ForeignKey("permissoes.id")),
)



class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email : Mapped[str] = mapped_column(unique=True)
    nome : Mapped[str]
    hashed_password : Mapped[str]
    is_ativo : Mapped[bool]
    
    orgao_id: Mapped[int] = mapped_column(ForeignKey("orgaos.id"))
    orgao: Mapped[Orgao] = relationship(back_populates="usuarios")
    perfis: Mapped[List["Perfil"]] = relationship(secondary=user_perfil)
    tickets : Mapped[List["Ticket"]] = relationship(back_populates="usuario")

class Perfil(Base):
    __tablename__ = "perfis"

    id: Mapped[int] = mapped_column(primary_key=True)
    title :  Mapped[str] = mapped_column()
    description : Mapped[str] = mapped_column()

    permissoes: Mapped[List["Permissao"]] = relationship(secondary=perfil_permissao)
    users: Mapped[List["User"]] = relationship(secondary=user_perfil)


class Permissao(Base):
    __tablename__ = "permissoes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)