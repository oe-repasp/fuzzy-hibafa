from app.db import conn
import mariadb

cur=conn.cursor()

my_query="select * from events"

cur.execute(my_query)

records=cur.fetchall()


for sor in records:
    print('{:40}: {:5} {:4} '.format(sor[1],"value",sor[2]))
