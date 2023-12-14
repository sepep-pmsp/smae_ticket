
from ..exceptions.api_smae import SessaoInativa

def login_required(func):
    '''Realiza login caso o endpoint da API requeira'''

    def wrapper(*args, **kwargs):

        #extraindo user e senha do obj
        self = args[0]
        user=self.user
        passw=self.passw

        try:
            return func(*args, **kwargs)
        except SessaoInativa:
            
            #se tiver inativa, loga de novo com user e senha
            self.session.login(user, passw)
            return func(*args, **kwargs)        

    return wrapper


def json_resp(func):
    '''Parseia a resposta como json'''

    def wrapper(*args, **kwargs):

        resp = func(*args, **kwargs)

        return resp.json()
    
    return wrapper