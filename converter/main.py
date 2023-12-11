from __future__ import annotations

from db import query
from csvgenerator.csvgenerator import CSVGenerator
# from gui import gui
from gui import grid4

def main():
    oQ = query.Queries()
    tables = oQ.get_tablenames()
    app = grid4.MyApp(tables)
    app.MainLoop()
    # print(get_tablenames(session=session(cnf.db)))
    # print(get_table_contents(session=session(cnf.db), tablename='users'))

    fieldnames = oQ.get_table_column_names(tablename='users')
    content = oQ.get_table_contents(tablename='users')
    CSVGenerator('users.csv', fieldnames=fieldnames, content=content)

if __name__ == '__main__':
    main()