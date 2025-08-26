-- 1. Создаем ч/з create новую таблицу departments
CREATE TABLE Departments (
DepartmentID SERIAL PRIMARY KEY, DepartmentName VARCHAR(50) UNIQUE NOT NULL, Location VARCHAR(50)
);

-- 2. Добавляем новый столбец email  в таблицу employees ч/з alter 
ALTER TABLE Employees 
ADD COLUMN Email VARCHAR(100);

-- 3. Заполняем email ч/з update+set переводом FN и LN  в нижний регистр 
UPDATE Employees SET Email = (LOWER(FirstName), '.', LOWER(LastName), '@gmail.com');

-- Добавляем ограничение constraint дляя unique к столбцу email ч/з alter 
ALTER TABLE Employees ADD CONSTRAINT unique_email UNIQUE (Email);

-- 4. Переименовываем столбец location в табл. departments также ч/з alter 
ALTER TABLE Departments RENAME COLUMN Location TO OfficeLocation;