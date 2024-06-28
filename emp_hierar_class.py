# Employee hierarchy program Using class.

class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary
        self.landline = ''
        self.manager = None

def print_employee(emp):
    print(f'Name: {emp.name}')
    print(f'Designation: {emp.designation}')
    print(f'Salary: {emp.salary}')
    print(f'Landline: {emp.landline}')



# Existing employees
emp1 = Employee('Manibalan', 'Junior Software Engineer', 50000)
emp2 = Employee('Judith', 'Software Engineer', 60000)
emp3 = Employee('Saranya', 'Team Lead', 70000)
emp1.manager = emp3
emp2.manager = emp3

# Additional employees
emp4 = Employee('Rani', 'Senior Software Engineer', 80000)
emp5 = Employee('Pranav', 'Project Manager', 90000)
emp6 = Employee('Arun', 'CTO', 120000)#CTO stands for Chief Technology Officer
emp4.manager = emp3
emp5.manager = emp3
emp3.manager = emp6  # Saranya now reports to Arun
emp6.manager = None  # Arun is the top-level manager

# Store all employees in a list
employees = [emp1, emp2, emp3, emp4, emp5, emp6]

# Print hierarchy for each employee
for emp in employees:
    # print('x' * 20)
    print('Employee Hierarchy:')
    print('-' * 20)
    current_emp = emp
    while current_emp is not None:   
        print_employee(current_emp)
        current_emp = current_emp.manager
    print('\n')
        
        

  
   

