from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional

from .database import Base
#evitando import circular
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .chamado import Chamado
    from .tags import Assunto, NivelUrgencia, Complexidade
    from .sla import SLABasico

from .cross_tables import chamado_ticket


class StatusTicket(Base):
    __tablename__ = "status_ticket"

    id: Mapped[int] = mapped_column(primary_key=True)
    status : Mapped[str] = mapped_column(unique=True)
    desc : Mapped[str]
    is_ativo : Mapped[bool]
    tickets : Mapped[List["Ticket"]] = relationship()


    
class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    is_ativo: Mapped[bool]
    desc: Mapped[str]

    #relacionamentos
    status_id: Mapped[int] = mapped_column(ForeignKey("status_ticket.id"))
    status: Mapped[StatusTicket] = relationship(back_populates="tickets")

    assunto_id: Mapped[int] = mapped_column(ForeignKey('assuntos.id'))
    assunto: Mapped["Assunto"] = relationship(back_populates='tickets_relacionados')

    chamados: Mapped[List["Chamado"]] = relationship(secondary=chamado_ticket, back_populates='tickets')

    urgencia_id: Mapped[int] = mapped_column(ForeignKey('niveis_urgencia.id'))
    urgencia: Mapped["NivelUrgencia"] = relationship(back_populates='tickets_relacionados')

    complexidade_id: Mapped[int] = mapped_column(ForeignKey('niveis_complexidade.id'))
    complexidade: Mapped["Complexidade"] = relationship(back_populates='tickets_relacionados')

    #eh o sla original associado ao ticket
    sla_basico_id: Mapped[int] = mapped_column(ForeignKey('slas.id'))
    sla_basico: Mapped["SLABasico"] = relationship(back_populates='tickets_relacionados')
    #eh o sla real, associado a eventos que podem fazer com que o SLA aumento ou diminua de tempo
    sla_real: Mapped[float]
