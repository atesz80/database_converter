from __future__ import annotations

from db import query
from csvgenerator.csvgenerator import CSVGenerator
from gui import gui

def main():
    # app = gui.MyApp()
    # app.MainLoop()
    # print(get_tablenames(session=session(cnf.db)))
    # print(get_table_contents(session=session(cnf.db), tablename='users'))
    oQ = query.Queries()
    fieldnames = oQ.get_table_column_names(tablename='users')
    content = oQ.get_table_contents(tablename='users')
    CSVGenerator('users.csv', fieldnames=fieldnames, content=content)

if __name__ == '__main__':
    main()