#a program that stores and manages student records

class Student:
  #the basic student class
    def __init__(self, name, house, lastgrade, prefername, dbirth, schoolclass, detention, lname ):
        self.name = name
        self.house = house
        self.lastgrade = lastgrade
        self.prefername = prefername
        self.dbirth = dbirth
        self.schoolclass = schoolclass
        self.detention = detention
        self.lname = lname

#now i spend my days creating getters and setters


    def set_lastgrade(self, lastgrade):
      self.lastgrade = lastgrade

    def set_detention(self, detention):
      self.detention = detention

    def set_schoolclass(self,schoolclass):
      self.schoolclass = schoolclass

andy = Student("andrew", "evans", "9", "andy", "17 9 24", "12F", "False", "crawford")
print(andy.prefername)


