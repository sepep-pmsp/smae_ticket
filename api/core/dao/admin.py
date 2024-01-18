from sqlalchemy.orm import Session

from ..models.auth import Perfil, Permissao
from ..models.estrutura_administrativa import Orgao, TipoOrgao
from ..models.users import User

from .decorators import rollback_operational_error

from typing import List

@rollback_operational_error('insert tipo_orgao')
def create_tipo_orgao(db: Session, tipo:str, desc:str)->TipoOrgao:

    model = TipoOrgao
    obj = model(tipo=tipo, desc=desc)
    #ativando o obj
    obj.is_ativo=True

    db.add(obj)
    db.commit()

    return obj


@rollback_operational_error('get tipo_orgao')
def get_tipo_orgao(db:Session, tipo_orgao_id:int)->TipoOrgao:

    model = TipoOrgao
    query = db.query(model)
    query.filter(model.id==tipo_orgao_id)
    
    return query.one()

@rollback_operational_error('insert orgao')
def create_orgao(db: Session, sigla:str, nome:str, tipo_orgao_id:int)->Orgao:

    #buscando o tipo de orgao
    tipo_orgao = get_tipo_orgao(db, tipo_orgao_id)

    model = Orgao
    obj = model(sigla=sigla, nome=nome, tipo_orgao=tipo_orgao)
    #ativando o obj
    obj.is_ativo=True

    db.add(obj)
    db.commit()

    return obj

@rollback_operational_error('insert permissao')
def create_permissao(db: Session, title:str, desc:str)->Permissao:

    model = Permissao
    obj = model(title=title, desc=desc)
    #ativando o obj
    obj.is_ativo=True

    db.add(obj)
    db.commit()

    return obj

@rollback_operational_error('get permissao')
def get_permissao(db:Session, permissao_id:int)->Permissao:

    model = Permissao
    query = db.query(model)
    query.filter(model.id==permissao_id)
    
    return query.one()

@rollback_operational_error('insert perfil')
def create_perfil(db: Session, title:str, desc:str, id_permissoes:List[int])->Perfil:

    permissoes = [get_permissao(id) for id in id_permissoes]

    model = Perfil
    obj = model(title=title, desc=desc, permissoes=permissoes)

    obj.is_ativo=True
    
    db.add(obj)
    db.commit(obj)

    return obj

@rollback_operational_error('insert user')
def create_user(db: Session, sigla:str)->User:
    pass