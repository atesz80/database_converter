from db import query
from csvgenerator.csvgenerator import CSVGenerator


class Converter(object):

    """ Az adatbázis táblák konvertálása .csv formátumba"""

    def __init__(self, tables: list) -> None:

        """ Konstruktor """

        self.tables = tables

    def converter(self) -> None:

        """ A metódus végzi el táblák mentését csv fájlokba """

        for table in self.tables:
            filename = f'{table}.csv'
            oQuery = query.Queries()
            fieldnames = oQuery.get_table_column_names(table)
            content = oQuery.get_table_contents(table)
            oCSVGenerator = CSVGenerator(filename=filename,
                                         fieldnames=fieldnames,
                                         content=content)
            oCSVGenerator.csv_generator()
