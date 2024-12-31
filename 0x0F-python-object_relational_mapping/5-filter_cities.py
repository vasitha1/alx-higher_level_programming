#!/usr/bin/python3

import MySQLdb
import sys


def main():
    searched_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    query = """
            SELECT cities.name
            FROM cities
            INNER JOIN states ON states.id=cities.state_id
            WHERE states.name = %s
            """
    cursor.execute(query, (searched_name,))

    results = cursor.fetchall()

    tmp = list(row[0] for row in results)
    print(*tmp, sep=", ")

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()