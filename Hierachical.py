# Task1:
# Define the base class person 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_personal_details(self):
        return f"Name: {self.name}, Age: {self.age}"
    
# Task2:
# Define the class Employee
class Employee(Person):
    def __init__(self, name, age,employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employeee_details(self):
         personal_details = self.display_personal_details()
         return f"{personal_details},Employee ID: {self.employee_id}, Salary:{self.salary:.2f}"
    
# Taks 3:
# Define Class manager
class Manager(Person):
    def __init__(self, name, age, department, team_size):
        super().__init__(name, age)
        self.department = department
        self.team_size = team_size

    def display_manager_details(self):
        personal_details = self.display_personal_details()
        return f"{personal_details}, Department: {self.department}, Team size: {self.team_size}"

# Task4:
# Object from the manager class
if __name__ =="__main__":
    employee = Employee("Employee", 30, "E12345", 50000)
    manager = Manager("manager",40, "Sales", 12)
    print("Manager Details:")
    print(manager.display_manager_details())
    print("Employee Details:")
    print(employee.display_employeee_details())
