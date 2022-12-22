#!/usr/bin/python3
""" Create a connection to a MySQL Server"""


if __name__ == "__main__":
    import sys
    import MySQLdb
    connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3], charset="utf8")
    cursor = connect.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
    FROM cities \
    INNER JOIN states ON cities.state_id = states.id \
    WHERE BINARY states.name = '{}' \
    ORDER BY cities.id".format(sys.argv[4]))
    str = ""
    for row in cursor.fetchall():
        str += row[1] + ", "
    print(str[:-2])
    cursor.close()
    connect.close()
