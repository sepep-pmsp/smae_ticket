from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional

from .database import Base

#evitando import circular
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    #import circular aqui
    from .tickets import Ticket
    from .chamado import Chamado
from .sla import SLABasico

from .cross_tables import chamado_assunto

class Assunto(Base):
    __tablename__ = "assuntos"

    id: Mapped[int] = mapped_column(primary_key=True)
    assunto : Mapped[str] = mapped_column(unique=True)
    desc : Mapped[str]
    #flag para identificar assunto tecncio para nao aparecer para usuario final
    is_tecnico: Mapped[bool]
    is_ativo : Mapped[bool]


    tickets_relacionados : Mapped[Optional[List["Ticket"]]] = relationship()
    chamados_relacionados : Mapped[Optional[List["Chamado"]]] = relationship(secondary=chamado_assunto)


class NivelUrgencia(Base):
    __tablename__ = "niveis_urgencia"

    id: Mapped[int] = mapped_column(primary_key=True)
    escala : Mapped[str] = mapped_column(unique=True)
    grau: Mapped[int]
    desc : Mapped[str]
    
    is_ativo : Mapped[bool]

    tickets_relacionados : Mapped[Optional[List["Ticket"]]] = relationship()
    slas_relacionados : Mapped[Optional[List["SLABasico"]]] = relationship()

class Complexidade(Base):
    __tablename__ = "niveis_complexidade"

    id: Mapped[int] = mapped_column(primary_key=True)
    escala : Mapped[str] = mapped_column(unique=True)
    grau: Mapped[int]
    desc : Mapped[str]
    
    is_ativo : Mapped[bool]

    tickets_relacionados : Mapped[Optional[List["Ticket"]]] = relationship()
    slas_relacionados : Mapped[Optional[List["SLABasico"]]] = relationship()