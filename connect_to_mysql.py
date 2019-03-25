import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='IPADDR',
                                       database='DB',
                                       port='PORT',
                                       user='USERNAME',
                                       password='PASSWORD')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()
