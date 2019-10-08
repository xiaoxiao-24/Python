''' Install package: pip install psycopg2 '''

import psycopg2

conn_string = "host='dbd.gdrpi.fr' dbname='EDU' user='postgres' password='gdrp1&L@tifi'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()
cur.execute('''select * from "VFAM" limit 10;''')
rows = cur.fetchall()

# 1) print the first variable of each line
for row in rows:
	print(row[0])

# 2) print the first line
print(rows[0])

# 3) print all
print(rows)