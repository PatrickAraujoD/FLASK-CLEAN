from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class BDConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def getEngine(self):
        """Return connection engine
        :param: None
        :return: engine connetion to DataBase
        """
        print(self.__connection_string)
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        self.session_maker = sessionmaker()
        self.session = self.session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
