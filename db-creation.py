import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user="root", password="", database="rdg_db")

mycursor = mydb.cursor(buffered=True)

command = "INSERT INTO `person`(`ID`, `lastname`, `firstname`, `number_of_dependents`) VALUES (%s, %s, %s, %s)"

employee = [(5,"iftikhar","mahnoor",6)]
mycursor.executemany(command, employee)

mydb.commit()
mycursor.close()
mydb.close()