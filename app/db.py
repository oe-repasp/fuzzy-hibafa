import mariadb
import sys


# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="fuzzy",
        password="fuzzydbpass",
        host="localhost",
        port=3306,
        database="fuzzyfta"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)



