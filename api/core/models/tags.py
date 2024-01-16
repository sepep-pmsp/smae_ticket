from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional, Union

from .database import Base

#evitando import circular
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    #import circular aqui
    from .tickets import Ticket, ticket_assunto
    from .chamado import Chamado, chamado_assunto

class Assunto(Base):
    __tablename__ = "Assunto"

    id: Mapped[int] = mapped_column(primary_key=True)
    assunto : Mapped[str] = mapped_column(unique=True)
    desc : Mapped[str]
    is_ativo : Mapped[bool]
    tickets_relacionados : Mapped[Optional[List"Ticket"]] = relationship(secondary=ticket_assunto)
    chamados_relacionados : Mapped[Optional[List"Chamado"]] = relationship(secondary=ticket_assunto)