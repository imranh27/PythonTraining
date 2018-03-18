
# Delete from sqlite database
import sqlite3
from sqlite3 import Error


# create connection
def create_connection(db_file):

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def delete_from(conn, idin):

    sql = 'DELETE FROM User WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (idin,) )


def delete_all(conn):

    sql = 'DELETE FROM User'
    cur = conn.cursor()
    cur.execute(sql)


# run program
def main():
    database = '/Users/imranh/Documents/Programming/PythonTraining/FlaskTutorial/microblog/app.db'
    userid = 2

    conn = create_connection(database)

    with conn:
        delete_from(conn, userid)   # delete one row
        # delete_all(conn)           # delete all rows


if __name__ == '__main__':
    main()