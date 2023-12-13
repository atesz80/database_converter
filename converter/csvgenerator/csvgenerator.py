import os
import csv
from csv import QUOTE_ALL


class CSVGenerator(object):

    """ Az osztály a csv file-ok generálásához szükséges. """

    def __init__(self,
                 filename: str,
                 fieldnames: list,
                 content: list,
                 path: str = 'csv_files') -> None:

        """ Konstruktor """

        self.path = path
        self.filename = filename
        self.fieldnames = fieldnames
        self.content = content

    def csv_generator(self):

        """ A metódus CSV file-t generál az adatbázis tábla tartalmáról """

        with open(os.path.join(self.path, self.filename),
                  'w',
                  newline='') as csvfile:
            writer = csv.DictWriter(csvfile,
                                    fieldnames=self.fieldnames,
                                    delimiter=";",
                                    quotechar='"',
                                    quoting=QUOTE_ALL)
            writer.writeheader()
            if self.content is not None:
                for row in self.content:
                    writer.writerow(row)
