#o chamado é o cara reclamando do problema
# o ticket é uma "penteada" no chamado identificando e tipificando problemas
# um chamado pode ter mais de um problema, logo, mais de um ticket

# a relacao entre chamado e ticket eh nao obrigatoria
# nao precisa ser um ticket novo - o chamado pode ser atribuido um ticket ja existente - caso: varias pessoas reclamam sobre uma mesma coisa

# o chamado soh eh resolvido quando tiver resolvido todos os tickets
# para que isso funcione, precisamos de Etapas no chamado - recebido, analise, tratamento - porque tem uma hora que tem que parar de criar ticket

# o usuario pode fechar o chamado quando ele quiser
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional

#evitando import circular
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .tickets import Ticket
from .cross_tables import chamado_assunto, chamado_ticket
from .database import Base
from .users import User
from .tags import Assunto



class Chamado(Base):

    __tablename__ = 'chamados'

    id: Mapped[int] = mapped_column(primary_key=True)
    desc: Mapped[str]
    is_ativo : Mapped[bool]

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped["User"] = relationship(back_populates='chamados')

    tickets: Mapped[Optional[List["Ticket"]]] = relationship(secondary=chamado_ticket, back_populates='chamados')
    assuntos: Mapped[List["Assunto"]] = relationship(secondary=chamado_assunto, back_populates='chamados_relacionados')
    