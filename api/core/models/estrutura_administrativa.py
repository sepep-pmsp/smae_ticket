from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, Optional

from .database import Base
#evitando import circular
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .users import User



class TipoOrgao(Base):
    __tablename__ = "tipos_orgao"

    id: Mapped[int] = mapped_column(primary_key=True)
    tipo : Mapped[str] = mapped_column(unique=True)
    desc : Mapped[str]
    is_ativo : Mapped[bool]
    orgaos: Mapped[Optional[List["Orgao"]]] = relationship()
    
class Orgao(Base):
    __tablename__ = "orgaos"

    id: Mapped[int] = mapped_column(primary_key=True)
    sigla : Mapped[str] = mapped_column(String(10))
    nome : Mapped[str]
    is_ativo : Mapped[bool]

    tipo_orgao_id: Mapped[int] = mapped_column(ForeignKey("tipos_orgao.id"))
    tipo_orgao: Mapped["TipoOrgao"] = relationship(back_populates="orgaos")
    usuarios : Mapped[Optional[List["User"]]] = relationship()


