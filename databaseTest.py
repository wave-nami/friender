import pyodbc
# the DSN value should be the name of the entry in odbc.ini, not freetds.conf
cnxn = pyodbc.connect('DSN=MYMSSQL;UID=SA;PWD=YourStrong@Passw0rd')
crsr = cnxn.cursor()
rows = crsr.execute("select @@VERSION").fetchall()
print(rows)
crsr.close()
cnxn.close()