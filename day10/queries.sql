CREATE TABLE departments(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	department_name TEXT NOT NULL);
	
CREATE TABLE employees(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	employee_name TEXT NOT NULL,
	salary INTEGER,
	department_id INTEGER);

INSERT INTO departments(department_name)
VALUES ('HR'),('sales'),('backend'),('AI');

INSERT INTO employees (employee_name,salary,department_id)
VALUES ('giri',45000,3),
('arun',45000,3),
('praveen',29000,1),
('rakesh',36000,2),
('sanjay',40000,4),
('albert',47000,2),
('surya',65000,4),
('vijay',35000,1);

SELECT employee_name,department_name
FROM employees JOIN departments
ON employees.department_id = departments.id;

SELECT employee_name,salary,department_name
FROM employees JOIN departments
ON employees.department_id = departments.id
WHERE department_name='AI';

SELECT department_name,avg(salary)
FROM departments JOIN employees
ON employees.department_id = departments.id
GROUP BY department_name;

SELECT department_name,avg(salary)
FROM departments JOIN employees
ON employees.department_id = departments.id
GROUP BY department_name
HAVING avg(salary)> 40000;