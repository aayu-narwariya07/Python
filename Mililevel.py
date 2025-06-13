class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal_details(self):
        return f"Name:,{self.name}, Age: {self.age}"
    
# Task2:
# Define the class Employee
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_details(self):
        personal_details = self.display_personal_details()
        return f"{personal_details}, Employee ID: {self.employee_id}, Salary: {self.salary:.2f}"
    
# Taks 3:
# Define the class manager
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department, team_size):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def display_manager_details(self):
        employee_details = self.display_employee_details()
        return f"{employee_details}, Department: {self.department}, Team Size: {self.team_size}"

# Task4:
if __name__ =="__main__":
    manager = Manager("Ramar Bose", 45, "M12345",95000, "Sales", 10)
    print("Manager Details:")
    print(manager.display_manager_details())
