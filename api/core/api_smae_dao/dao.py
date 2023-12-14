from .api_session import APISession
from .decorators import login_required, json_resp

class DAO:

    def __init__(self, host_api:str, user:str, passw:str)->None:

        self.session = APISession(host_api)
        self.user=user
        self.passw=passw

    def login(self, user:str, passw:str)->None:

        self.session.login(user, passw)

    @json_resp
    @login_required
    def user_data(self):

        return self.session.get('minha-conta')

    

