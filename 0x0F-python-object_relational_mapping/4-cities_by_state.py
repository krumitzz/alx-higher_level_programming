#!/usr/bin/python3
"""
lists all cities from the database
"""
import sys
import MySQLdb

if __name__ == '__main__':

    host = 'localhost'
    port = 3306
    u, passwd, db_name = (sys.argv[1],
                          sys.argv[2],
                          sys.argv[3])

    # connect to db
    db = MySQLdb.connect(host, u, passwd, db_name, port=port)
    cur = db.cursor()

    # query db
    query_string = """SELECT cities.id, cities.name, states.name
                        FROM states
                        INNER JOIN cities ON states.id = cities.state_id
                        ORDER BY cities.id ASC"""
    cur.execute(query_string)

    # print result
    results = cur.fetchall()
    for row in results:
        print(row, end='\n')

    # close db and connection
    cur.close()
    db.close()
