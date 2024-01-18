from sqlalchemy.exc import OperationalError
from ..exceptions.db_exceptions import DBError

def rollback_operational_error(anotacao_erro:str):

    def decorator(dao_func):
        def wrapper(*args, **kwargs):

            try:
                return dao_func(*args, **kwargs)
            
            except OperationalError as e:
                #a Session sempre tem que ser o primeiro argumento!
                db = args[0]
                db.rollback()
                msg_erro = f'Erro ao realizar {anotacao_erro}: {str(e)}'
                raise DBError(msg_erro)
            
        return wrapper
    
    return decorator
