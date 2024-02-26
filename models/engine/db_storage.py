"""Clase para gestionar el almacenamiento."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self) -> None:
        """Inicializa una instancia de DBStorage."""
        ABAST_MYSQL_USER = getenv('ABAST_MYSQL_USER')
        ABAST_MYSQL_PWD = getenv('ABAST_MYSQL_PWD')
        ABAST_MYSQL_HOST = getenv('ABAST_MYSQL_HOST')
        ABAST_MYSQL_DB = getenv('ABAST_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(ABAST_MYSQL_USER,
                                             ABAST_MYSQL_PWD,
                                             ABAST_MYSQL_HOST,
                                             ABAST_MYSQL_DB))

    def reload(self):
        """
        Este método creará las tablas solo la primera vez
        durante el ciclo de vida de este proyecto.

        Luego creará las sesiones para hacer consultas a las tablas.
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def new(self, obj):
        self.__session.add(obj)
