import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="fuzzy",
        password="4248LAGA4ELA",
        host="localhost",
        port=3306,
        database="fuzzyfta"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
