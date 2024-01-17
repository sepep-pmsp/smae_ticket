
from sqlalchemy import Column, ForeignKey, Table

from .database import Base


chamado_assunto = Table(
    "chamado_assunto",
    Base.metadata,
    Column("ticket_id", ForeignKey("chamados.id")),
    Column("assunto_id", ForeignKey("assuntos.id")),
)


chamado_ticket = Table(
    "chamado_ticket",
    Base.metadata,
    Column("chamado_id", ForeignKey("chamados.id")),
    Column("ticket_id", ForeignKey("tickets.id")),
)

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
