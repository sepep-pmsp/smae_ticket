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

    def __identificar_sessao_inativa(self, resp:Response)->None:

        if resp.status_code == 401:
            resp = resp.json()
            if resp['message']=='Sessão não está mais ativa' or resp['message']=='Acesso Não Autorizado.':
                raise SessaoInativa(str(resp))
            else:
                raise HTTPError(str(resp))
        
        return resp
    
    def build_url(self, endpoint:str)->str:

        return self.host+endpoint

    def get_token(self, user:str, passw:str)->str:

        url = self.build_url('login')

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
        
    def get(self, endpoint:str, *args, **kwargs)->Any:
        

        url = self.build_url(endpoint)
        resp = self.session.get(url, *args, **kwargs)
        self.__identificar_sessao_inativa(resp)

        return resp

    def post(self, endpoint:str, *args, **kwargs)->Any:

        url = self.build_url(endpoint)
        resp = self.session.post(url, *args, **kwargs)
        self.__identificar_sessao_inativa(resp)

        return resp  
        
    
        
        

    