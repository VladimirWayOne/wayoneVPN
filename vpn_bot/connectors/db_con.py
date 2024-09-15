import logging
from utils.logger import setup_logger
import psycopg2
import sys
sys.path.append("../utils")
db_logger = setup_logger('db_log', 'db_log.log', level=logging.DEBUG)


class PgSQLCon:
    def __init__(self, host, usr, pwd, port=5423, dbname='postgres'):
        self.__dbname = dbname
        self.__host = host
        self.__usr = usr
        self.__pwd = pwd
        self.__port = port
        self._connection = None
        self._cursor = None
        self.__connect()

    def __connect(self):
        try:
            self._connection = psycopg2.connect(
                dbname=self.__dbname, user=self.__usr, password=self.__pwd, host=self.__host, port=self.__port)
            self._cursor = self._connection.cursor()
        except Exception as e:
            self._connection = None
            db_logger.error(
                f"Couldn't connect to DataBase. Error:\r\n{e}", exc_info=True)

    def get_cursor(self):
        if self._connection and self._cursor:
            return self._cursor

    def __connection_health_check(self):
        if self._connection and self._cursor:
            try:
                self._cursor.execute('SELECT 1')
                return True
            except Exception as e:
                self.__connect()
                self.__connection_health_check()
        else:
            return False

    def select(self, query: str, params: tuple = None) -> list:
        if self.__connection_health_check():
            try:
                db_logger.debug(f"query:\r\n{query}\r\nparams:\r\n{params}")
                self._cursor.execute(query=query, vars=params)
                return self._cursor.fetchall()
            except Exception as e:
                db_logger.error(
                    f"Couldn't execute select \r\n{query}", exc_info=True)

    def insert(self, query: str, params: tuple = None):
        if self.__connection_health_check():
            try:
                db_logger.debug(f"query:\r\n{query}\r\nparams:\r\n{params}")
                self._cursor.execute(query=query, vars=params)
                self.__commit()
            except Exception as e:
                db_logger.error(
                    f"Couldn't execute insert \r\n{query}", exc_info=True)

    def __commit(self):
        self._connection.commit()
