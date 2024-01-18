from sqlalchemy.exc import OperationalError


class DBError(OperationalError):
    pass