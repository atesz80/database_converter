import csv
from csv import QUOTE_ALL

class CSVGenerator(object):

    def __init__(self, filename: str, fieldnames: list, content: list) -> None:
        
        """ Konstruktor """

        self.filename = filename
        self.fieldnames = fieldnames
        self.content = content

    @classmethod
    def csv_generator(self):

        """ A metódus CSV file-t generál az adatbázis tábla tartalmáról """

        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames, delimiter=";", quotechar='"', quoting=QUOTE_ALL)
            writer.writeheader()
            for row in self.content:
                writer.writerow(row)