# Class Name
# Blueprint for creating Employee objects

#from .exceptions import InvalidSalaryError
#from .exceptions import InvalidSalaryError

from .exceptions import (InvalidSalaryError,InvalidNameError) # Importing Multiple Exceptions


class Employee:

    # Constructor Method
    # Runs automatically when object is created

    def __init__(self, emp_id, name, salary):

        # self -> current object reference

        # Attributes / Instance Variables
        # Data stored inside object 

        # name validation

        if name.isalpha() == False:

            raise InvalidNameError(
                "Name should contain only alphabets"
            )

        # salary Validation

        if salary < 0:

            raise InvalidSalaryError(
                "Salary cannot be negative"
            )

        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    # Instance Method / Member Function
    # Used to perform actions on object data

    def display(self):

        # f-string
        # Used to insert variables into string

        print(f"""
Employee ID : {self.emp_id}
Employee Name : {self.name}
Salary : {self.salary}
""")