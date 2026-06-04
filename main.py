# main.py

# Package Import
# Importing Employee through package
# from employees.employee import Employee ## absolute import  ## is possible but we have already created a __init__.py which will directly allow the employee class to be imported from the package
# from employees import Employee relative import because we already create a __init_.py which will directly allow the employee class to be imported from the package


# Package Import
# Employee comes through __init__.py
#from employees.employee import Employee

# Absolute Import
from database.dp import connect

# Import Constant
from config import COMPANY_NAME


# Package Import

from employees import Employee  #relative inmport

#absolute import


from employees.exceptions import (
    InvalidSalaryError,
    InvalidNameError
)

import logger
import logging


print(f"Welcome to {COMPANY_NAME}")
connect()
# Employee Data


employee_data = [

    (101, "Yuvaraj", 50000),     # Valid

    (102, "Ram123", 40000),      # Name Error (contains numbers)

    (103, "Kumar@", 60000),      # Name Error (special character)

    (104, "Sam", 45000),         # Name Length Error (if you kept len<=4 validation)

    (105, "Krishna", -5000),     # Salary Error

    (106, "Arun", 70000),        # Name Length Error (length=4)

    (107, "Vignesh", 80000)      # Valid

]



# Store Valid Employees

employees = []


# Create Employees

for emp_id, name, salary in employee_data:

    try:

        emp = Employee(
            emp_id,
            name,
            salary
        )

        employees.append(emp)

        print(
            f"Employee {emp_id} Created Successfully"
        )

        logging.info(
        f"Employee {emp_id} Created Successfully"
    )

    except InvalidSalaryError as e:

        logging.error(
        f"Employee {emp_id} Salary Error : {e}"
    )


        print(f"Salary Error : {e}")
    
    except InvalidNameError as e:

        logging.error(
        f"Employee {emp_id} Name Error : {e}"
    )
        
        print(f"Name Error : {e}")



print("\nVALID EMPLOYEES\n")


# Display Valid Employees

for emp in employees:

    emp.display()



#
##heeey hi"""