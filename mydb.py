import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="avazbek2002@w#",
)

cursor = database.cursor()

print("All Done")