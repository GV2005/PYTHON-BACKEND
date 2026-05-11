CREATE TABLE sales (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	employee TEXT NOT NULL,
	department TEXT,
	city TEXT,
	amount INTEGER);
	
SELECT * FROM sales;

INSERT INTO sales(employee,department,city,amount)
VALUES  ('giri','sales','chennai',75000),
		('harish','production','chennai',65000),
		('arun','sales','coimbatore',85000),
		('giri','production','chennai',45000),
		('parthiban','hr','coimbatore',55000),
		('santhos','sales','chennai',67000),
		('giri','software','bangalore',15000),
		('arun','transport','bangalore',25000),
		('albert','sales','trichy',35000),
		('richard','hr','salem',95000);
		
SELECT sum(amount) FROM sales;

SELECT avg(amount) FROM sales;

SELECT max(amount) FROM sales;

SELECT min(amount) FROM sales;

SELECT count(*) FROM sales;

SELECT department,sum(amount) FROM sales GROUP BY department;

SELECT city,avg(amount) FROM sales GROUP BY city;

SELECT department,sum(amount)
FROM sales
GROUP BY department
HAVING sum(amount)>=100000;

SELECT city,avg(amount) FROM sales
GROUP BY city
HAVING avg(amount)>50000;

SELECT department,count(*) FROM sales
GROUP BY department;

SELECT department, SUM(amount)
FROM sales
GROUP BY department
ORDER BY SUM(amount) DESC
LIMIT 1;

SELECT city,count(*)
FROM sales
GROUP BY city
HAVING count(*)>=2;

SELECT department,avg(amount)
FROM sales
GROUP BY department
HAVING avg(amount)<50000;