from app.db import conn

cur=conn.cursor()

cur.execute("select @@hostname")


for i in cur:
    print(i)