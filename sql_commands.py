import sqlite3

def insert_day(conn, day):
    sql = """ INSERT INTO days(date_id,day_of_week)
            VALUES(julianday(?),?) """

    cursor = conn.cursor()
    cursor.execute(sql, day)
    conn.commit()
    return cursor.lastrowid

def insert_smokes(conn, smokes):
    sql = """ INSERT INTO smokes(number_id,time,date_id)
            VALUES(?,julianday(?),julianday(?)) """

    cursor = conn.cursor()
    cursor.execute(sql, smokes)
    conn.commit()
    return cursor.lastrowid

def insert_drinks(conn, drinks):
    sql = """ INSERT INTO drinks(number_id,name,alcoholic,quantity,cost,date_id)
            VALUES(?,?,?,?,julianday(?)) """

    cursor = conn.cursor()
    cursor.execute(sql, drinks)
    conn.commit()
    return cursor.lastrowid

def insert_breakfast(conn, breakfast):
    sql = """ INSERT INTO breakfast(date_id,time,dish,location,cost)
            VALUES(julianday(?),julianday(?),?,?,?) """

    cursor = conn.cursor()
    cursor.execute(sql, breakfast)
    conn.commit()
    return cursor.lastrowid

def insert_lunch(conn, lunch):
    sql = """ INSERT INTO lunch(date_id,time,dish,location,cost)
            VALUES(julianday(?),julianday(?),?,?,?) """

    cursor = conn.cursor()
    cursor.execute(sql, lunch)
    conn.commit()
    return cursor.lastrowid

def insert_dinner(conn, dinner):
    sql = """ INSERT INTO dinner(date_id,time,dish,location,cost)
            VALUES(julianday(?),julianday(?),?,?,?) """

    cursor = conn.cursor()
    cursor.execute(sql, dinner)
    conn.commit()
    return cursor.lastrowid

def insert_medication(conn, med):
    sql = """ INSERT INTO medication(date_id,time)
            VALUES(julianday(?),julianday(?)) """

    cursor = conn.cursor()
    cursor.execute(sql, med)
    conn.commit()
    return cursor.lastrowid