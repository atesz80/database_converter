from __future__ import annotations
from db.db import get_db_session as session
from db.config import config as cnf


class Queries(object):

    """ Az osztály az SQL lekérdezésekhez szükséges """


    def __init__(self, dbconfig: str = cnf.db) -> None:

        """ Konstruktor """
        
        self.session=session(dbconfig=dbconfig)


    def get_tablenames(self) -> list | None:

        """ A metódus visszatér a táblanevek listájával """

        query = {}

        query['query'] = """
            SHOW TABLES;
        """

        query['parameter'] = ({})

        rows = self.session.read(query['query'] % query['parameter'])

        if (rows):
            return [row for row in rows[0].values()]
        
        else:
            return None

        
    def get_table_column_names(self, tablename: str) -> list:

        """ A metódus visszatér a tábla mezőneveivel """

        query = {}

        query['query'] = f"""
            SHOW COLUMNS FROM {tablename};
        """

        query['parameter'] = ({'tablename': tablename})

        rows = self.session.read(query['query'] % query['parameter'])

        if (rows):
            return [value for row in rows for key, value in row.items() if key == 'Field']
        
        else:
            return None


    def get_table_contents(self, tablename: str) -> list | None:

        """ A metódus visszatér a megadott tábla tartalmával """

        query = {}

        query['query'] = f"""
            SELECT * FROM {tablename};
        """

        query['parameter'] = ({})

        result = self.session.read(query['query'] % query['parameter'])

        if (result):
            return result
        
        else:
            return None
