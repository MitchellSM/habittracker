import sqlite3
from sqlite3 import Error

class Database(object):
    """ Singleton object for creating a single database object """

    class __database:
        """ Object for manipulating a database """
        def __init__(self, file_name=None):
            self.file_name = file_name
        
        def get_file_name(self):
            return self.file_name
        
        def set_file_name(self, name):
            self.file_name = name

        def __str__(self):
            return repr(self) + str(self.val)
        
        def create_connection(self):
            """ create a database connection to a SQLite database """
            conn = None
            try:
                conn = sqlite3.connect(self.file_name)
                print(sqlite3.version)
            except Error as e:
                print(e)
            
            return conn

        def insert(conn, table_info, table_data):
            """ 
            table_info is a string with the format table_name(pk_col_name, col_name_1, ..., col_name_N)
            to represent the table definition.
            """

            sql = ''' INSERT INTO ''' + table_info 
            + ''' VALUES(''' + "?," * (len(table_data)-1) + "?)"
            cursor = conn.cursor()
            cursor.execute(sql, table_data)
            conn.commit()
        
        def update(conn, table_name, table_data_dict, cond=None):
            col_names = list(table_data_dict.keys())
            col_value = list(table_data_dict.values())

            sql = ''' UPDATE ''' + table_name + '''\nSET '''

            for i, k in enumerate(col_names):
                sql += k + ''' = ?''' 
                sql += "\n" if i == len(col_names)-1 else ",\n"
                
            if cond:
                sql += "WHERE " + cond
            
            cursor = conn.cursor()
            cursor.execute(sql, col_value)
            conn.commit()
        
        def query(conn, sql_stmt, table_data):
            """ General query function for complex SQL statements """
            cursor = conn.cursor()
            cursor.execute(sql_stmt, table_data)
            conn.commit()

    __instance = None
    def __new__(cls, filename):
        if not Database.__instance:
            Database.__instance = Database.__database(filename)
        return Database.__instance

## DEBUG uncomment for testing ##
# db = Database(r"habittracker.db")


