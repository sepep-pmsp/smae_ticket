from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional

from .database import Base
#evitando import circular
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .users import User
    from .tags import Assunto


### colocar complexidade e urgencia no Ticket
### sla vai estar associado a isso - para saber quantas horas eh para cada combinacao de complexidade e urgencia
### tem que ver a questao dos niveis de atendimento que estao no contrato tambem
### colocar um  atributo de delay_sla no ticket que eh um float e a aplicacao vai colocando delay conforme for necessario para nao estourar o SLA
### vai ter um atributo sla_real que tem os acréscimos e é modificavel e um atributo SLA original qeu registra para aquele ticket o tempo esperado original com base no  banco
    


###soh chamdo vai ser muitos pra muitos, ticket pode ter um assunto soh
ticket_assunto = Table(
    "ticket_assunto",
    Base.metadata,
    Column("ticket_it", ForeignKey("tickets.id")),
    Column("assunto_id", ForeignKey("assuntos.id")),
)


class StatusTicket(Base):
    __tablename__ = "status_ticket"

    id: Mapped[int] = mapped_column(primary_key=True)
    status : Mapped[str] = mapped_column(unique=True)
    desc : Mapped[str]
    is_ativo : Mapped[bool]
    tickets : Mapped[List["Ticket"]] = relationship(back_populates='status')


    
class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)

    #relacionamentos
    status_id: Mapped[int] = mapped_column(ForeignKey("status_ticket.id"))
    status: Mapped[StatusTicket] = relationship(back_populates="tickets")
    assuntos: Mapped[List["AssuntoTicket"]] = relationship(secondary=ticket_assunto)

    usuario_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    usuario : Mapped["User"] = relationship(back_populates='tickets')