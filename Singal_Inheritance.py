class Employee:
    def __init__(self, name, employee_id, salary):
        """
        Initializes the Employee class with common employee details such as name, ID, and salary
        """
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """
        Displys the employee's details.
        """
        return f"Employee Name: {self.name}\nEmployee ID: {self.employee_id}\nsalary: {self.salary:.2f}"
     
# task2:
# Define the derived class manager
class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        """
        Initializes the Manager class, which inherits from Employee and the size attribute.
        """
        super().__init__(name, employee_id, salary)
        self.team_size = team_size
    def disply_details(self):
        """
        Displays the manager's details, inculuding team size.
        """
        employee_details = super().display_details()
        return f"{employee_details}\nTeam Size: {self.team_size}"
    
    # Task3:
    # Instantiate object from base and Derived Classes
if __name__=="__main__":
    # create an instance of Employee
    employee = Employee("Employee1", "E001",50000)
    manager = Manager("Manager", "M456", 80000, 10)
    print("Employee Details:")
    print(employee.display_details())
    print("\nManager Details:")
    print(manager.display_details())
