from requests import Session, Response
from requests.exceptions import HTTPError
from ..exceptions.api_smae import SenhaUserErrado, SessaoInativa, ContaBloqueada
from typing import Any

class APISession:

    def __init__(self, api_host:str)->None:

        self.host = api_host
        self.session = Session()
        self.token = None

    def __solve_login_errors(self, resp:Response)->None:
        
        if resp.status_code == 401:
            resp = resp.json()
            if resp['message']=='email| E-mail ou senha inválidos':
                raise SenhaUserErrado(str(resp))
            if resp['message']=="email| Conta está bloqueada, acesse o e-mail para recuperar a conta":
                raise ContaBloqueada(str(resp))
            if resp['message']=='Sessão não está mais ativa':
                raise SessaoInativa(str(resp))
            
        raise HTTPError(str(resp.json()))


    def get_token(self, user:str, passw:str)->str:

        endpoint = 'login'
        url = self.host+endpoint

        data = {
        "email": user,
        "senha": passw
        }

        with self.session.post(url, data=data) as r:
            
            if r.status_code == 200:
                return r.json()['access_token']                
            self.__solve_login_errors(r)
            
    def login(self, user:str, passw:str)->None:

        try:
            token = self.get_token(user, passw)
            self.session.headers['Authorization'] = f'Bearer {token}'
            self.token = token
            return True
        except SenhaUserErrado:
            return False
        except Exception as e:
            raise e
        
    def get(self, *args, **kwargs)->Any:
        
        return self.session.get(*args, **kwargs)

    def post(self, *args, **kwargs)->Any:

        return self.session.post(*args, **kwargs)    
        
    
        
        

    