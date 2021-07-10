class Employee:
    def __init__(self,name,age,salary,gender):
         self.name= name
         self.age= age
         self.salary= salary
         self.gender= gender
    def show_employee_details(self):
        print("Name is ",self.name)
        print("age is ",self.age)
        print("salary ",self.salary)
        print("gener is ",self.gender)

e1 = Employee("Ram",166,56666,"Male")
print(e1.show_employee_details())
