# Python Backend learning process

## Day 1 - Advanced Functions
Covered:
- Parameters / Arguments
- Return
- Default Arguments
- Keyword Arguments
- *args
- **kwargs
- Scope / Global
- Lambda
- Recursion
- Closures
- Decorators

Status: Completed ✅

## Day 2 - Modules & Packages

Covered:

* import module
* from module import function
* alias import (`as`)
* custom modules
* multiple modules
* packages
* `__init__.py`
* package-level exports
* `json`
* `datetime`
* `uuid`
* `os`

Built:

* `helpers/math_utils.py`
* `helpers/string_utils.py`
* `helpers/validator.py`
* `helpers/data_utils.py`
* `main.py` integrating all modules

Status: Completed ✅

## Day 3 - Practical OOP

Covered:

* Class & Object
* Attributes
* Constructor (`__init__`)
* Methods
* Inheritance
* Method Overriding
* Encapsulation
* Class Variables
* `__str__()`

Built:

* Patient class
* Doctor class
* Appointment class
* Main integration file

Status: Completed ✅

## Day 4 - Exceptions + Validation

Covered:

* try / except
* Specific exceptions
* `as e`
* else
* finally
* raise
* Custom exceptions
* Validation functions
* assert

Built:

* Custom exception classes
* Validators module
* User registration validation system

Status: Completed ✅

## Day 5 - File Handling + JSON

Covered:

* File read (`r`)
* File write (`w`)
* File append (`a`)
* `with open(...)`
* JSON save (`json.dump`)
* JSON load (`json.load`)
* File exception handling (`FileNotFoundError`)
* JSON empty file handling (`JSONDecodeError`)
* List of dictionaries in JSON

Built:

* Read / write / append practice files
* JSON profile save & load
* Safe file handler
* Local User Database System (`UserManager` with add / view / find user)

Status: Completed ✅

## Day 6 - Type Hints, venv & Clean Project Structure

Covered:

* Function type hints (`a: int -> int`)
* Variable type hints
* Collection type hints (`list[str]`, `dict[str, str]`)
* Optional types (`Optional[str]`)
* Virtual Environment (`venv`)
* pip package management
* `requirements.txt`
* Clean package/project structure
* Running package modules (`python -m app.main`)

Built:

* Type hint practice files
* Virtual environment setup
* Requirements file generation
* Structured mini app:

  * `models/User`
  * `validators/user_validator.py`
  * `services/user_service.py`
  * `utils/helpers.py`
  * `main.py`

Key Learnings:

* Difference between module import vs function import
* Avoid file name = function name confusion
* Proper class naming (`User`, not `Users` for single object)
* Professional root-level execution for package projects

Status: Completed ✅

## Day 7 - SQL Basics

Covered:

* Databases, Tables, Rows, Columns
* SQL syntax fundamentals
* CREATE TABLE
* INSERT INTO
* SELECT queries
* WHERE filtering
* ORDER BY sorting
* LIMIT results
* UPDATE rows
* DELETE rows
* ALTER TABLE (rename table)
* Auto Increment Primary Key behavior

Built:

* SQLite practice database (`backend_learning.db`)
* Students table
* Teachers table
* Multiple CRUD operations using SQL

Key Learnings:

* Difference between SQL language and database software
* Primary keys should not be manually edited
* Deleted IDs are not usually reused (Auto Increment behavior)
* SQL CRUD operations are core backend building blocks

Status: Completed ✅

## Day 8 - SQL CRUD & Query Mastery

### Topics Covered

* Advanced WHERE filtering
* AND / OR / NOT operators
* IN operator
* BETWEEN operator
* LIKE pattern matching
* Alias using AS
* Multiple conditions in a single WHERE clause
* ORDER BY with LIMIT
* Safe UPDATE operations
* Safe DELETE operations
* Difference between DELETE and DROP TABLE

### Hands-on Work

Created:

* `company.db`
* `employees` table
* `queries.sql`

Practiced:

* Multi-condition filtering
* Pattern-based search queries
* Salary range filtering
* City-based filtering
* Updating records dynamically
* Deleting records safely
* Writing independent SQL challenge queries

### Mini Challenge Completed

Queries solved independently:

* Highest salary employee
* Employees not in Chennai
* Employees whose name contains `"r"`

### Key Learning

Moved from remembering SQL syntax → writing SQL queries independently.

Status: Completed ✅

## Day 9 - GROUP BY, HAVING & Aggregate Functions

### Topics Covered

* Aggregate functions:

  * SUM()
  * AVG()
  * MAX()
  * MIN()
  * COUNT()
* GROUP BY
* HAVING
* Grouped analytics queries
* ORDER BY with grouped results
* SQL query execution flow

### Hands-on Work

Created:

* `analytics.db`
* `sales` table
* `queries.sql`

Practiced:

* Department-wise total sales
* City-wise average sales
* Employee count per department
* Filtering grouped data using HAVING
* Finding highest grouped totals
* Aggregated reporting queries

### Key Learnings

* WHERE filters rows before grouping
* HAVING filters groups after grouping
* GROUP BY creates analytical summaries
* Aggregate functions simplify analytics operations
* SQL query execution order matters

### Status

Completed ✅

## Day 10 - SQL Joins

### Topics Covered

* Relational database concepts
* Table relationships using IDs
* INNER JOIN
* Multi-table queries
* Filtering joined data
* Aggregates with joins
* GROUP BY on joined tables
* HAVING with joins

### Hands-on Work

Created:

* `joins.db`
* `departments` table
* `employees` table
* `queries.sql`

Practiced:

* Connecting employee and department data
* Fetching related data across tables
* Department-wise salary analytics
* Filtering joined records
* Aggregate analysis on relational data

### Key Learnings

* Tables are connected using matching IDs
* JOIN combines related table data
* Relational databases reduce repeated information
* Aggregates and grouping work across joined tables

### Status

Completed ✅

## Day 11 - SQLite with Python

### Topics Covered

* SQLite integration using Python
* Database connection using `sqlite3`
* Executing SQL queries through Python
* Fetching database records
* Updating records using Python
* Deleting records using Python
* Commit and connection handling
* Python-driven database CRUD operations

### Hands-on Work

Created:

* `company.db`
* `main.py`

Implemented:

* Database connection
* Table creation using Python
* Inserting records into SQLite database
* Fetching records using `fetchall()`
* Filtering records with SQL conditions
* Updating employee salaries
* Deleting employee records
* Verifying database updates through Python

### Key Learnings

* `sqlite3.connect()` creates or connects to existing database
* `commit()` is required after INSERT / UPDATE / DELETE operations
* `fetchall()` returns data as tuples
* SQL queries can be executed directly from Python
* Python can fully control database CRUD operations
* Missing WHERE in UPDATE affects all rows

### Mini Backend CRUD Practice

Built a small Python-based employee database workflow:

* Show employees
* Add employee
* Update salary
* Delete employee
* Display updated records

### Status

Completed ✅

## Day 12 - PostgreSQL Setup & Basics

### Topics Covered

* PostgreSQL installation
* pgAdmin setup
* PostgreSQL server connection
* Creating databases in PostgreSQL
* Creating tables using PostgreSQL
* CRUD operations in PostgreSQL
* JOIN queries in PostgreSQL
* PostgreSQL vs SQLite syntax differences

### Hands-on Work

Created:

* `company_db`
* `employees` table
* `departments` table

Practiced:

* INSERT operations
* SELECT queries
* UPDATE operations
* DELETE operations
* JOIN queries across tables
* ORDER BY usage in PostgreSQL

### Key Learnings

* PostgreSQL is a database server, unlike SQLite file-based databases
* PostgreSQL uses `SERIAL PRIMARY KEY` instead of `AUTOINCREMENT`
* Row order is not guaranteed without `ORDER BY`
* SQL concepts transfer across databases with minor syntax differences
* pgAdmin acts as a GUI for managing PostgreSQL

### Status

Completed ✅

## Day 13 - Python with PostgreSQL

### Topics Covered

* PostgreSQL integration with Python
* `psycopg2` setup and usage
* Connecting Python to PostgreSQL
* PostgreSQL CRUD operations through Python
* Executing SQL queries using Python
* Fetching PostgreSQL records in Python

### Hands-on Work

Created:

* `main.py`

Implemented:

* PostgreSQL database connection using `psycopg2`
* Table creation using Python
* INSERT operations
* SELECT queries
* UPDATE operations
* DELETE operations
* Fetching and printing PostgreSQL records

### Key Learnings

* `psycopg2` is used for PostgreSQL integration in Python
* PostgreSQL uses `SERIAL PRIMARY KEY`
* PostgreSQL workflow is similar to SQLite with different drivers
* Python can fully control PostgreSQL databases
* Backend applications communicate with databases through drivers

### Status

Completed ✅

## Day 14 - FastAPI with PostgreSQL

### Topics Covered

* FastAPI with PostgreSQL integration
* Using `psycopg2` inside FastAPI
* Building CRUD APIs with PostgreSQL
* Executing PostgreSQL queries through API endpoints
* REST API development with FastAPI

### Hands-on Work

Created:

* `main.py`

Implemented:

* PostgreSQL connection inside FastAPI
* GET API to fetch employees
* POST API to add employees
* PATCH API to update employee salary
* DELETE API to remove employees
* Database commit handling
* API response handling

### Key Learnings

* FastAPI can directly interact with PostgreSQL databases
* PostgreSQL uses `%s` placeholders in `psycopg2`
* REST APIs perform CRUD operations through database queries
* PATCH is used for partial updates
* Backend APIs connect frontend requests with databases

### APIs Built

* `GET /employees`
* `POST /addemployee`
* `PATCH /update_employee/{id}`
* `DELETE /delete_employee/{id}`

### Status

Completed ✅

## Day 15 - Database Schema Design

### Topics Covered

* Database schema design concepts
* Entity and relationship modeling
* One-to-One relationships
* One-to-Many relationships
* Many-to-Many relationships
* Foreign key concepts
* Normalization basics
* Relational database architecture

### Hands-on Understanding

Designed conceptual schema structures for:

* Hospital Management System
* Patients and Doctors relationships
* Department-based structures
* Prescription and medicine relationships

### Key Learnings

* Schema design focuses on organizing data efficiently
* Tables should reduce duplicate/redundant data
* Relationships connect entities logically
* Foreign keys maintain relational integrity
* One-to-Many relationships are very common in backend systems
* Good schema design improves scalability and maintainability

### Relationship Types Learned

* One-to-One (1:1)
* One-to-Many (1:M)
* Many-to-Many (M:M)

### Status

Completed ✅



## FastAPI Learning Progress

### Completed Topics

* FastAPI Introduction
* Running FastAPI with Uvicorn
* Swagger Docs (`/docs`)
* ReDoc (`/redoc`)
* Path Parameters
* Query Parameters
* Request Body with Pydantic Models
* Data Validation
* Form Data Handling
* File Uploads (`UploadFile`)

### Concepts Practiced

* GET Requests
* POST Requests
* Dynamic Routes
* Query Filtering
* Request Parsing
* Automatic Validation
* File Handling in APIs

### Status

FastAPI Fundamentals Completed ✅
(First 6 sections / 12 lectures from Udemy course)

### FastAPI Update - Advanced Concepts

#### Completed Topics

* Dependency Injection fundamentals
* Function-level dependencies
* Class-level dependencies
* Global dependencies
* Sub-dependencies (nested dependencies)
* Yield-based dependencies (setup / cleanup pattern)
* Session handling
* Rate limiting

#### Concepts Practiced

* Reusable dependency functions
* Shared authentication / validation logic
* Request lifecycle management using `yield`
* Dependency chaining
* Managing session-based request state
* Understanding request limits / throttling mechanisms
* Cleaner route architecture with modular reusable components

#### Key Understanding

* Reduced repeated code across routes
* Improved API structure using dependency injection
* Learned practical session handling patterns
* Understood API protection using rate limiting
* Better understanding of production backend design concepts

#### Hands-on

* Implemented code examples for all dependency injection levels
* Practiced session management workflows
* Built rate-limit protected API examples

#### Status

FastAPI Advanced Concepts — Completed ✅

### FastAPI Update - Database & Authentication

#### Completed Topics

* SQLite integration using `sqlite3`
* Database CRUD operations in FastAPI
* JWT Authentication
* Token generation and validation
* Protected routes using authentication dependencies
* Authentication workflow implementation

#### Concepts Practiced

* Connecting FastAPI routes with database layer
* Executing SQL queries through Python
* User authentication with JWT tokens
* Securing endpoints
* Token-based request authorization
* End-to-end API flow (request → validation → auth → DB → response)

#### Certification

Completed **FastAPI Full Course – Python Framework | Beginner to Advanced** (Udemy) ✅ 

#### Status

FastAPI Backend Fundamentals + Authentication — Completed ✅




## Projects Built

### Ecommerce API Testing Project (Postman)

**Folder:** `postman/ecommerce-api-testing/`

Covered:

* Postman GUI tour
* Workspace & Collections
* First API request
* GET / POST / PUT / PATCH / DELETE
* Headers
* Query Parameters
* Request Body
* Login API
* Token / Authorization
* Real-world API testing

---

## Upcoming

* PostgreSQL
* FastAPI
* Healthcare backend capstone
