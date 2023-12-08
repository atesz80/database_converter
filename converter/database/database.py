import mysql.connector
from mysql.connector import Error


class SQL(object):

    __instance = None
    __host = None
    __user = None
    __password = None
    __database = None
    __session = None
    __connection = None
    __config = None
    connection = None

    def __init__(self, db_config: dict) -> None:

        self.__config = db_config

    def open(self):

        try:
            cnx = mysql.connector.connect(
                **self.__config, auth_plugin='mysql_native_password'
            )
            self.__connection = cnx
            self.__session = cnx.cursor()

            # print("MySQL Database connection successful")
            return cnx

        except Error as err:
            print(f"Error: '{err}'")

    def close(self):

        try:
            self.__session.close()
            self.__connection.close()
            # print('DB closed')

        except Error as err:
            print(f"Error: '{err}'")

    def isopen(self):

        try:
            if self.__connection.is_connected is None:
                print("Not connected")
                exit

            if self.__connection.is_connected():
                print('Is connected')
                return True

            else:
                print('Not connected')
                return False

        except Error as err:
            print(f"Error: '{err}'")
            return False

    def read(self, query):

        result = None

        try:
            self.open()
            result = []
            self.__session.execute(query)
            desc = self.__session.description
            column_names = [col[0] for col in desc]

            for row in self.__session.fetchall():
                result.append(dict(zip(column_names, row)))

            self.close()
            return result

        except Error as err:
            print(f"Error: '{err}'")
            self.close()

    def insert(self, query):

        # result = None
        try:
            self.open()
            self.__session.execute(query)
            # result = self.__session.fetchall()
            self.__connection.commit()
            self.close()
            return True

        except Error as err:
            print(f"Error: '{err}'")
            self.close()

    def insert_test(self, query):

        # result = None
        try:
            self.open()
            self.__session.execute(query)
            # result = self.__session.fetchall()
            # self.__connection.commit()
            self.close()
            return True

        except Error as err:
            print(f"Error: '{err}'")
            self.close()


def get_db_session(dbconfig):

    return SQL(dbconfig)
