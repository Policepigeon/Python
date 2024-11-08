#a program that stores and manages student records
#importing the sql linker
import sqlite3
con = sqlite3.connect("Student DB")
cur = con.cursor()
#this is needed the first time you run the program to create the database
#cur.execute("CREATE TABLE student(name, lastname, prefername, dbirth, house, lastgrade, detention)")

class Student:
  #the basic student class
    def __init__(self, name, house, lastgrade, prefername, dbirth, schoolclass, detention, lastname ):
        self.name = name
        self.house = house
        self.lastgrade = lastgrade
        self.prefername = prefername
        self.dbirth = dbirth
        self.schoolclass = schoolclass
        self.detention = detention
        self.lastname = lastname

#now i spend my days creating getters and setters


    def set_lastgrade(self, lastgrade):
      self.lastgrade = lastgrade

    def set_detention(self, detention):
      self.detention = detention

    def set_schoolclass(self,schoolclass):
      self.schoolclass = schoolclass

andy = Student("andrew", "evans", "9", "andy", "17 9 24", "12F", "False", "crawford")
#taking the input for the student
student = input("what is the student's name?")
student = Student(student, input("\n What is the student's house?"), input("\n What is the student's last grade?"), input("\n What is the student's preferred name?"), )
print(andy.prefername)

#Allows the user to input their desired query, for example a search for users. do input sanitation later.
res = cur.execute(input("Please input your SQLite query"))
print(res.fetchall())

#closing the cursor and connection to the db after commiting the changes to the database
con.commit()
cur.close()
con.close()