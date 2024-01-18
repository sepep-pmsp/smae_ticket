from pydantic import BaseModel
from typing import Optional, List

class TipoOrgao:

    tipo: str
    desc: str

class Orgao:

    sigla: str
    nome: str
    tipo_orgao: TipoOrgao

class OrgaoUsuarios(Orgao):

    pass
    #usuarios: List[Usuario]