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
