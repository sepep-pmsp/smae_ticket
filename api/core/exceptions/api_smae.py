from requests.exceptions import HTTPError

class SenhaUserErrado(HTTPError):
    pass

class SessaoInativa(HTTPError):
    pass

class ContaBloqueada(HTTPError):
    pass