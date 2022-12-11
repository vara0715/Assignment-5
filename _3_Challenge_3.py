# Challenge 3: Implement the Complete Student Class

class Student:

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    
    def setRollNumber(self,rollnumber):
        self.__rollnumber = rollnumber
    def getRollNumber(self):
        return self.__rollnumber

student = Student()
student.setName("Pratham")
data = student.getName()
print(data)
student.setRollNumber(04)
data = student.getRollNumber()
print(data)
