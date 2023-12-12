from __future__ import annotations
import mysql.connector
from mysql.connector import Error


class SQL(object):

    """

        Az osztály az adatbázis eléréséhez szükésges.
        MYSQL adatbázis kapcsolatot valósít meg
        és a metódusokkal tudjuk lekérdezni vagy módosítani illetve
        beilleszteni a táblákba a rekordokat.

    """

    _session = None
    _connection = None
    _config = None
    connection = None

    def __init__(self, db_config: dict) -> None:

        """ Konstruktor """

        self._config = db_config

    def open(self) -> object | str:

        """ A metódus az adatbázis kapcsolatot valósítja meg """

        try:
            cnx = mysql.connector.connect(
                **self._config, auth_plugin='mysql_native_password'
            )
            self._connection = cnx
            self._session = cnx.cursor()

            print("MySQL Database connection successful")
            return cnx

        except Error as err:
            print(f"Error: '{err}'")

    def close(self) -> None:

        """ A metódus az adatbázis kapcsolat lezárásához """

        try:
            self._session.close()
            self._connection.close()
            print('DB closed')

        except Error as err:
            print(f"Error: '{err}'")

    def isopen(self) -> None:

        """ Az adatbázis kapcsolat létrejött-e """

        try:
            if self._connection.is_connected is None:
                print("Not connected")
                exit

            if self._connection.is_connected():
                print('Is connected')
                return True

            else:
                print('Not connected')
                return False

        except Error as err:
            print(f"Error: '{err}'")
            return False

    def read(self, query: str) -> list | str:

        """ A metódus az SQL lekérdezésekhez szükséges (SELECT) """

        result = None

        try:
            self.open()
            result = []
            self._session.execute(query)
            desc = self._session.description
            column_names = [col[0] for col in desc]

            for row in self._session.fetchall():
                result.append(dict(zip(column_names, row)))

            self.close()
            return result

        except Error as err:
            print(f"Error: '{err}'")
            self.close()

    def insert(self, query: str) -> bool | str:

        """
            A metódus az adatok adatbázis táblákba való beillesztését
            és azok módosítását oldja meg
        """

        try:
            self.open()
            self._session.execute(query)
            self._connection.commit()
            self.close()
            return True

        except Error as err:
            print(f"Error: '{err}'")
            self.close()


def get_db_session(dbconfig: str) -> SQL:

    """ Adatbázis session létrehozása """

    return SQL(dbconfig)
