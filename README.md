# aquaflask

# Company Employee API
=======================

This project is a Flask-based RESTful API to manage company employees. It supports operations like fetching employee details, adding new employees, updating existing employees, and deleting employees.

#Project Structure
==================

- `api.py`: The main Flask application file containing all API endpoints.
- `tests.py`: Unit tests for the API endpoints.

#Installation Instructions
==========================

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/company-employee-api.git
   cd company-employee-api

-Set up a virtual environment (optional but recommended): python -m venv (name of your venv)
# On cmd, use `venv\Scripts\activate` to activate the script of the environment


intall dependencies
-'pip install -r requirements.txt'

Set Up Mysql database

 -Create a database named company.

 -Create a table named employee with the necessary columns.

 -Update the database credentials in api.py if needed.


CREATE DATABASE company;
=======================

USE company;

CREATE TABLE employee (

    SSN INT PRIMARY KEY,
    Fname VARCHAR(50),
    Minit CHAR(10),
    Lname VARCHAR(50),
    Bdate DATE,
    Address VARCHAR(100),
    Sex CHAR(1),
    Salary DECIMAL(10,2),
    Super_ssn INT,
    DL_id VARCHAR(20)
);
Set SSN into AUTO INCREMENT(AI) at your workbench so you dont have to worry for setting the SSN of employee.

Running the Application
To run the Flask application, use the following command:
   python api.py
The application will be accessible at http://127.0.0.1:5000/.

API Endpoints
==============
#1. Get All Employees

   Endpoint: /employee

   Method: GET

   Description: Fetches details of all employees.

POSTMAN COMMAND(http://127.0.0.1:5000/employee)

   Response Example:


  {
    
    "SSN": 888665555,
    "Fname": "James",
    "Minit": "A",
    "Lname": "Doe",
    "Bdate": "1980-01-01",
    "Address": "123 Test St",
    "Sex": "M",
    "Salary": 60000.00,
    "Super_ssn": 123456789,
    "DL_id": "D1234567"
  }


#2. Get Employee by SSN

Endpoint: /employee/<int:ssn>

Method: GET

Description: Fetches details of an employee by SSN.

POSTMAN COMMAND(http://127.0.0.1:5000/employee/999887778)

   Response Example:
   {

      "SSN": 888665555,
      "Fname": "James",
      "Minit": "A",
      "Lname": "Doe",
      "Bdate": "1980-01-01",
     "Address": "123 Test St",
     "Sex": "M",
     "Salary": 60000.00,
     "Super_ssn": 123456789,
     "DL_id": "D1234567"
   }


#3. Add a New Employee

Endpoint: /employee

Method: POST

Description: Adds a new employee.

POSTMAN COMMAND(http://127.0.0.1:5000/employee)

Request Body Example:


   {

      "Fname": "James",
     "Minit": "A",
     "Lname": "Doe",
     "Bdate": "1980-01-01",
     "Address": "123 Test St",
     "Sex": "M",
     "Salary": 60000.00,
     "Super_ssn": 123456789,
     "DL_id": "D1234567"
   }


Response example

   {

     "message": "employee added successfully",
     "rows_affected": 1
   }


#4. Update an Employee

Endpoint: /employee/<int:ssn> 

Method: PUT 

Description: Updates details of an employee. 

POSTMAN COMMAND(http://127.0.0.1:5000/employee/999887780)

Request Body Example:

   {

     "Fname": "James",
     "Minit": "A",
      "Lname": "Smith",
     "Bdate": "1980-01-01",
     "Address": "123 Test St",
     "Sex": "M",
      "Salary": 65000.00,
     "Super_ssn": 123456789,
     "DL_id": "D1234567"
   }
 
 response example

   {

     "message": "Employee updated successfully",
     "rows_affected": 1
   }


#5. Delete an Employee

Endpoint: /employee/<int:ssn>

Method: DELETE

Description: Deletes an employee by SSN.

POSTMAN COMMAND (http://127.0.0.1:5000/employee/999887777)

Response Example:
   
   {

     "message": "employee deleted successfully",
     "rows_affected": 1
   }

To run the unit tests, use the following command:

(python -m unittest discover)

test.py(name of the python script)
=================================
   import unittest

   import warnings

   from api import app

   class MyAppTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_index_page(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "<p>Hello, World!</p>")

    def test_get_employees(self):
        response = self.app.get("/employee")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("James" in response.data.decode())

    def test_get_employee_by_id(self):
        response = self.app.get("/employee/888665555")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("James" in response.data.decode())

if __name__ == "__main__":
    unittest.main()

##Additional Information

Ensure your MySQL server is running and accessible.

Update any hardcoded values in the tests and code as per your actual database entries.

Feel free to contribute and open issues if you find any bugs or have suggestions for improvements!

Copy the above content and paste it into a file named `README.md` in your GitHub repository. This documentation will help others understand your project, set it up, and run it          correctly.

##LICENSED

[MIT](http://en.wikipedia.org/wiki/MIT_License) license.






