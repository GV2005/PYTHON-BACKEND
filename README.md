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
