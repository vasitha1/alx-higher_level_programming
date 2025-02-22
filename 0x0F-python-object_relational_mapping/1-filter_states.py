#!/usr/bin/python3
"""
This model is meant to print states and their corresponding ids
"""
import MySQLdb
import sys


def main():
    """This is the main function"""

    if len(sys.argv) == 4:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cursor = db.cursor()
        cursor.execute("""SELECT id, name FROM states WHERE name
                       LIKE 'N%' ORDER BY id ASC""")
        results = cursor.fetchall()

        if results:
            for row in results:
                print(row)

        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
