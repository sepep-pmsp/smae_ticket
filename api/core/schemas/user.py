from pydantic import BaseModel, EmailStr
from typing import Optional, List

from .estrutura_administrativa import Orgao
from .auth import Perfil

class UserBasico:

    email: EmailStr
    nome: str
    orgao: Orgao

class UserAuth(UserBasico):

    perfis: List[Perfil]