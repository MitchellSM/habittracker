import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    """ Create a new table using an open connection """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_day(conn, day):
    sql = """ INSERT INTO days(date_id,day_of_week)
            VALUES(julianday(?),?) """

    cursor = conn.cursor()
    cursor.execute(sql, day)
    conn.commit()
    return cursor.lastrowid

def create_smokes(conn, smokes):
    sql = """ INSERT INTO smokes(number_id,time,date_id)
            VALUES(?,julianday(?),julianday(?)) """

    cursor = conn.cursor()
    cursor.execute(sql, smokes)
    conn.commit()
    return cursor.lastrowid

def create_drinks(conn, drinks):
    sql = """ INSERT INTO drinks(number_id,name,alcoholic,quantity,cost,date_id)
            VALUES(?,?,?,?,julianday(?)) """

    cursor = conn.cursor()
    cursor.execute(sql, drinks)
    conn.commit()
    return cursor.lastrowid

def create_breakfast(conn, breakfast):
    sql = """ INSERT INTO breakfast(date_id,time,dish,location,cost)
            VALUES(julianday(?),julianday(?),?,?,?) """

    cursor = conn.cursor()
    cursor.execute(sql, breakfast)
    conn.commit()
    return cursor.lastrowid

def create_lunch(conn, lunch):
    sql = """ INSERT INTO lunch(date_id,time,dish,location,cost)
            VALUES(julianday(?),julianday(?),?,?,?) """

    cursor = conn.cursor()
    cursor.execute(sql, lunch)
    conn.commit()
    return cursor.lastrowid

def create_dinner(conn, dinner):
    sql = """ INSERT INTO dinner(date_id,time,dish,location,cost)
            VALUES(julianday(?),julianday(?),?,?,?) """

    cursor = conn.cursor()
    cursor.execute(sql, dinner)
    conn.commit()
    return cursor.lastrowid

def create_medication(conn, med):
    sql = """ INSERT INTO medication(date_id,time)
            VALUES(julianday(?),julianday(?)) """

    cursor = conn.cursor()
    cursor.execute(sql, med)
    conn.commit()
    return cursor.lastrowid

def _create_all_tables(db_name):
    """ Create all new tables in db """

    create_table_meds = """ CREATE TABLE IF NOT EXISTS medication (
                                date_id real PRIMARY KEY,
                                time real NOT NULL,
                                FOREIGN KEY (date_id) REFERENCES days (date_id)
                                ); """

    create_table_lunch = """ CREATE TABLE IF NOT EXISTS lunch (
                                date_id real PRIMARY KEY,
                                time real NOT NULL,
                                dish text,
                                location text,
                                cost integer,
                                FOREIGN KEY (date_id) REFERENCES days (date_id)
                                ); """

    create_table_dinner = """ CREATE TABLE IF NOT EXISTS dinner (
                                date_id real PRIMARY KEY,
                                time real NOT NULL,
                                dish text,
                                location text,
                                cost integer,
                                FOREIGN KEY (date_id) REFERENCES days (date_id)
                                ); """

    create_table_breakfast = """ CREATE TABLE IF NOT EXISTS breakfast (
                                    date_id real PRIMARY KEY,
                                    time real NOT NULL,
                                    dish text,
                                    location text,
                                    cost integer,
                                    FOREIGN KEY (date_id) REFERENCES days (date_id)
                                    ); """

    create_table_drinks = """ CREATE TABLE IF NOT EXISTS drinks (
                                number_id integer PRIMARY KEY,
                                name text NOT NULL,
                                alcoholic boolean NOT NULL CHECK (alcoholic IN (0,1)),
                                quantity text NOT NULL,
                                cost real,
                                date_id real,
                                FOREIGN KEY (date_id) REFERENCES days (date_id)
                                ); """

    create_table_smokes = """ CREATE TABLE IF NOT EXISTS smokes (
                                number_id integer PRIMARY KEY,
                                time real,
                                date_id real,
                                FOREIGN KEY (date_id) REFERENCES days (date_id)
                                ); """

    create_table_day = """ CREATE TABLE IF NOT EXISTS days (
                                date_id real PRIMARY KEY,
                                day_of_week text
                                );"""


    conn = create_connection(db_name)
    with conn:
        create_table(conn, create_table_day)
        create_table(conn, create_table_smokes)
        create_table(conn, create_table_drinks)
        create_table(conn, create_table_breakfast)
        create_table(conn, create_table_lunch)
        create_table(conn, create_table_dinner)
        create_table(conn, create_table_meds)

def main():

    db = r"/home/mitchell/Desktop/CODE/habittracker/habittracker.db"
    
    _create_all_tables(db)

if __name__ == '__main__':
    main()