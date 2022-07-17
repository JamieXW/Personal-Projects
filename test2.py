class Employee:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def introduction(self):
        return ("Hi my name is " + str(self.name) + " and I'm " + str(self.age) + " years old")

emp_1 = Employee('John', 36) 
emp_2 = Employee('Jack', 29) 

print(emp_2.introduction())