from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional

from .database import Base

#evitando import circular
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    #import circular aqui
    from .tags import NivelUrgencia, Complexidade
    from .tickets import Ticket


class SLABasico(Base):
    __tablename__ = "slas"

    id: Mapped[int] = mapped_column(primary_key=True)
    desc : Mapped[str]
    tempo_base: Mapped[int]
    is_ativo : Mapped[bool]

    urgencia_id: Mapped[int] = mapped_column(ForeignKey('niveis_urgencia.id'))
    urgencia: Mapped["NivelUrgencia"] = relationship(back_populates='slas_relacionados')

    complexidade_id: Mapped[int] = mapped_column(ForeignKey('niveis_complexidade.id'))
    complexidade: Mapped["Complexidade"] = relationship(back_populates='slas_relacionados')

    tickets_relacionados: Mapped[Optional[List["Ticket"]]] = relationship()