from sqlalchemy import create_engine


class BDConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self):
        self.__connection_string = "sqlite://storage.db"
        self.session = None

    def getEngine(self):
        """Return connection engine
        :param: None
        :return: engine connetion to DataBase
        """
        engine = create_engine(self.__connection_string)
        return engine
