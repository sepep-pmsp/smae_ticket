#o chamado é o cara reclamando do problema
# o ticket é uma "penteada" no chamado identificando e tipificando problemas
# um chamado pode ter mais de um problema, logo, mais de um ticket

# a relacao entre chamado e ticket eh nao obrigatoria
# nao precisa ser um ticket novo - o chamado pode ser atribuido um ticket ja existente - caso: varias pessoas reclamam sobre uma mesma coisa

# o chamado soh eh resolvido quando tiver resolvido todos os tickets
# para que isso funcione, precisamos de Etapas no chamado - recebido, analise, tratamento - porque tem uma hora que tem que parar de criar ticket

# o usuario pode fechar o chamado quando ele quiser
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional

from .database import Base
#evitando import circular
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .users import User
    from .tags import Assunto


chamado_assunto = Table(
    "chamado_assunto",
    Base.metadata,
    Column("ticket_it", ForeignKey("chamados.id")),
    Column("assunto_id", ForeignKey("assuntos.id")),
)

class Chamado:

    __tablename__ = 'chamados'

    id: Mapped[int] = mapped_column(primary_key=True)