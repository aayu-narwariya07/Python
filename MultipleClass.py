# Task1:
class Person:
    def __init__(self, name, age, roll_no):
        """
        Initialize the person class with person's name
        """
        self.name = name
        self.age = age
        self.roll_no = roll_no
    def greet(self):
        """
        Returns a greeting message with the person's name
        """
        return f"Hello, I'm {self.name, self.age, self.roll_no}"
    
# Define the Base Class Employee
class Employee:
    def __init__(self, employee_id):
        """
        Initializes the employee class with the employee's Id. 
        """
        self.employee_id = employee_id

    def get_employee_id(self):
        """
        Returns the employee ID
        """
        return self.employee_id
    
# Task3:
#  Define  the class menager
class Manager(Person, Employee):
    def __init__(self, name, employee_id,age, roll_no):
        """
        Initilaizes the menager class, which inherits from person and employee
        """
        Person.__init__(self, name,age,roll_no)
        Employee.__init__(self, employee_id)

# Taks4:
# class manager
if __name__ =="__main__":
    manager = Manager("Ramar Bose", "E12345", 32, 1)
    print(manager.greet())
    print("Age:",manager.age)
    print("Roll No:",manager.roll_no)
    print(f"Employee ID: {manager.get_employee_id()}")
        
