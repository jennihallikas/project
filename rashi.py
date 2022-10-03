import mysql.connector

connection = mysql.connector.connect(
         host='mysql.metropolia.fi',
         port= 3306,
         database='jenniheh',
         user='jenniheh',
         password='1234',
         autocommit=True
)



