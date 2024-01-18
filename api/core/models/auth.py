from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional

from .database import Base

#evitando import circular
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .users import User

from .cross_tables import user_perfil, perfil_permissao

class Perfil(Base):
    __tablename__ = "perfis"

    id: Mapped[int] = mapped_column(primary_key=True)
    title :  Mapped[str] = mapped_column(index=True)
    desc : Mapped[str]

    permissoes: Mapped[List["Permissao"]] = relationship(secondary=perfil_permissao)
    users: Mapped[Optional[List["User"]]] = relationship(secondary=user_perfil, back_populates='perfis')

    is_ativo: Mapped[bool]


class Permissao(Base):
    __tablename__ = "permissoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(index=True)
    desc: Mapped[str]

    is_ativo: Mapped[bool]