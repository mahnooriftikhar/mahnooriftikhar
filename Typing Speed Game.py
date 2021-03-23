"""import pygame
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="")

print(mydb)

if(mydb):
    print("Connection Successful!")
else:
    print("Unsuccessful")
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")