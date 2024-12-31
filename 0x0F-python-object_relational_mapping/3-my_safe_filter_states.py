#!/usr/bin/python3
"""
This model prints a model which is safe from sql injections
"""
import MySQLdb
import sys


def main():
    """The main function"""
    searched_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    query = "SELECT id, name FROM states WHERE name LIKE BINARY %s"
    cursor.execute(query, (searched_name,))

    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
