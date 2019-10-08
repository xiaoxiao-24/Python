''' Install package: pip install psycopg2 '''

import psycopg2

conn_string = "host='dbd.gdrpi.fr' dbname='EDU' user='postgres' password='gdrp1&L@tifi'"
#conn = psycopg2.connect(database = "EDU", user = "postgres", password = "gdrp1&L@tifi", host = "dbd.gdrpi.fr", port = "5432")
conn = psycopg2.connect(conn_string)
cur = conn.cursor()
cur.execute('''select * from "VFAM"  limit 10;''')
rows = cur.fetchall()
# 1) print the first variable of each line
for row in rows:
	print(row[0])
# 2) print the first line
print(rows[0])
# 3) print all
print(rows)

table = ["VFAM","VBEN"]
# exemple 1
for item in table:
	cur.execute('''select * from "''' + item + '''" limit 10;''')
	rows = cur.fetchall()
	for row in rows:
		print(row[0])
# exemple 2
for item in table:
	cur.execute('''select "DATE_MAJ", count(1) from "''' + item + '''" group by "DATE_MAJ";''')
	rows = cur.fetchall()
	for row in rows:
		print(row[0],row[1])	
		
# exemple 3
table = ["ARCH_VFAM","ARCH_VBEN"]
for item in table:
	cur.execute('''select "DATE_MAJ", count(1) from "''' + item + '''" where "DATE_MAJ" = (select max("DATE_MAJ") from "''' + item + '''") group by "DATE_MAJ";''')
	rows = cur.fetchall()
	for row in rows:
		print(row[0],row[1])	

	  
# exemple 4
conn2 = psycopg2.connect(database = "EDU", user = "postgres", password = "gdrp1&L@tifi", host = "dbp.gdrpi.fr", port = "5432")
cur = conn2.cursor()
table_lot1 = ["VFAM","VFAM_BDO","VBEN","VBEN_BDO","VADR","VMTT","VRGM","VDRG","VPRV"]
for item in table_lot1:
	cur.execute('''select "DATE_MAJ", count(1) from "''' + item + '''" group by "DATE_MAJ";''')
	rows = cur.fetchall()
	for row in rows:
		print(item,row[0],row[1])		
		
table_lot2 = ["VBDO_MAJ", "VBDO_MAJ_AG","VCPF","VCUR","VETA","VFMJ","VGRC_AUT_ADH","VGRC_AUT_CAN",
"VGRC_AUT_COD","VGRC_AUT_CPT","VGRC_AUT_ECA","VGRC_AUT_ETA","VGRC_AUT_IAM","VGRC_RCC_ASS","VIJP",
"VJOD","VJQL","VMAT","VMLL","VPBD","VPEC","VPRA","VRCI","VSG_CARTES","VSG_COMMANDES_CARTES"]
for item in table_lot2:
	cur.execute('''select "DATE_MAJ", count(1) from "''' + item + '''" group by "DATE_MAJ";''')
	rows = cur.fetchall()
	for row in rows:
		print(item,row[0],row[1])	

table_lot3 = ["ARCH_VBEN","ARCH_VBEN_BDO","ARCH_VFAM","ARCH_VFAM_BDO","ARCH_VADR","ARCH_VMTT","ARCH_VRGM","ARCH_VDRG","ARCH_VPRV","ARCH_VBDO_MAJ", 
"ARCH_VBDO_MAJ_AG","ARCH_VCPF","ARCH_VCUR","ARCH_VETA","ARCH_VFMJ","ARCH_VGRC_AUT_ADH","ARCH_VGRC_AUT_CAN","ARCH_VGRC_AUT_COD",
"ARCH_VGRC_AUT_CPT","ARCH_VGRC_AUT_ECA","ARCH_VGRC_AUT_ETA","ARCH_VGRC_AUT_IAM","ARCH_VGRC_RCC_ASS","ARCH_VIJP","ARCH_VJOD",
"ARCH_VJQL","ARCH_VMAT","ARCH_VMLL","ARCH_VPBD","ARCH_VPEC","ARCH_VPRA","ARCH_VRCI","ARCH_VSG_CARTES","ARCH_VSG_COMMANDES_CARTES"]
for item in table_lot3:
	cur.execute('''select "DATE_MAJ", count(1) from "''' + item + '''" where "DATE_MAJ" = (select max("DATE_MAJ") from "''' + item + '''") group by "DATE_MAJ";''')
	rows = cur.fetchall()
	for row in rows:
		print(item,row[0],row[1])	

		
# exemple 5
# 1)create table "TEST_STAT"	
# 2)insert données	
#list tables
table_benef_1 = ["VFAM","VFAM_BDO","VBEN","VBEN_BDO","VADR","VMTT","VRGM","VDRG","VPRV",
"VBDO_MAJ", "VBDO_MAJ_AG","VCPF","VCUR","VETA","VFMJ","VGRC_AUT_ADH","VGRC_AUT_CAN",
"VGRC_AUT_COD","VGRC_AUT_CPT","VGRC_AUT_ECA","VGRC_AUT_ETA","VGRC_AUT_IAM","VGRC_RCC_ASS","VIJP",
"VJOD","VJQL","VMAT","VMLL","VPBD","VPEC","VPRA","VRCI","VSG_CARTES","VSG_COMMANDES_CARTES"]

table_benef_2 = ["ARCH_VBEN","ARCH_VBEN_BDO","ARCH_VFAM","ARCH_VFAM_BDO","ARCH_VADR","ARCH_VMTT","ARCH_VRGM","ARCH_VDRG","ARCH_VPRV","ARCH_VBDO_MAJ", 
"ARCH_VBDO_MAJ_AG","ARCH_VCPF","ARCH_VCUR","ARCH_VETA","ARCH_VFMJ","ARCH_VGRC_AUT_ADH","ARCH_VGRC_AUT_CAN","ARCH_VGRC_AUT_COD",
"ARCH_VGRC_AUT_CPT","ARCH_VGRC_AUT_ECA","ARCH_VGRC_AUT_ETA","ARCH_VGRC_AUT_IAM","ARCH_VGRC_RCC_ASS","ARCH_VIJP","ARCH_VJOD",
"ARCH_VJQL","ARCH_VMAT","ARCH_VMLL","ARCH_VPBD","ARCH_VPEC","ARCH_VPRA","ARCH_VRCI","ARCH_VSG_CARTES","ARCH_VSG_COMMANDES_CARTES"]

conn = psycopg2.connect(database = "EDU", user = "postgres", password = "gdrp1&L@tifi", host = "dbd.gdrpi.fr", port = "5432")
cur = conn.cursor()
#create table
cur.execute('''CREATE TABLE public."TEST_STAT"
      ("tbl_name"	varchar(30)   NULL,
      "DATE_MAJ"	timestamp    NULL,
      "nb_ligne"	INT     NULL);''')
conn.commit()
# write benef
for item in table_benef_1:
	cur.execute('''select "DATE_MAJ", count(1) from "''' + item + '''" group by "DATE_MAJ";''')
	rows = cur.fetchall()
	for row in rows:	
		cur.execute("INSERT INTO \"TEST_STAT\" (\"tbl_name\",\"DATE_MAJ\",\"nb_ligne\") VALUES('"+item+"','"+row[0].strftime("%Y-%m-%d %H:%M:%S")+"',"+str(row[1])+");")
conn.commit()
# write arch_benef
for item in table_benef_2:
	cur.execute('''select "DATE_MAJ", count(1) from "''' + item + '''" where "DATE_MAJ" = (select max("DATE_MAJ") from "''' + item + '''") group by "DATE_MAJ";''')
	rows = cur.fetchall()
	for row in rows:	
		cur.execute("INSERT INTO \"TEST_STAT\" (\"tbl_name\",\"DATE_MAJ\",\"nb_ligne\") VALUES('"+item+"','"+row[0].strftime("%Y-%m-%d %H:%M:%S")+"',"+str(row[1])+");")
conn.commit()
conn.close()