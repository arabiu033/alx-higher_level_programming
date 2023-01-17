#!/usr/bin/python3
""" Create a connection to a MySQL Server"""


if __name__ == "__main__":
    import sys
    import MySQLdb
    connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3], charset="utf8")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY \
    name = '{}' ORDER BY id ASC".format(sys.argv[4]))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connect.close()
