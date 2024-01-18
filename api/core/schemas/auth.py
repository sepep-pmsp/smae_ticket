from pydantic import BaseModel
from typing import Optional, List

class Permissao:

    title: str
    desc: str

class Perfil:

    title: str
    desc: str

    permissoes: List[Permissao]