# aquaflask
# Company Employee API

This project is a Flask-based RESTful API to manage company employees. It supports operations like fetching employee details, adding new employees, updating existing employees, and deleting employees.

#Project Structure

- `api.py`: The main Flask application file containing all API endpoints.
- `tests.py`: Unit tests for the API endpoints.

#Installation Instructions

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


