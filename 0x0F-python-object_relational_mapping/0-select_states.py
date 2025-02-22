#!/usr/bin/python3
"""
This module selects id and name from the state database
"""
import MySQLdb
import sys


def main():
    """ Main function that runs when the file is run"""
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
