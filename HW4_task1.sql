-- 1. Вставляем двух сотрудников через insert 
INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES ('Max', 'Winston', 'HR', '50000.00');

INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES ('Liza', 'Chapman', 'IT', '80000.00');

-- 2. Выбираем через select всех сотрудников из табл. employees
SELECT * FROM Employees;

-- 3. Ч/з select выбираем firstname и lastname из определенного отдела IT
SELECT FirstName, LastName FROM Employees WHERE Department = 'IT';

-- 4. Обновляем зп ч/з update+set у элис смит 
UPDATE Employees SET Salary = 65000.00 WHERE FirstName = 'Alice' AND LastName = 'Smith';

-- 5. Удаляем сотрудника с lastname prince
-- Перед этим удалим зависимости сотрудника по фамилии, чтобы не нарушить внешний ключ 
DELETE FROM EmployeeProjects WHERE EmployeeID IN (
SELECT EmployeeID FROM Employees WHERE LastName = 'Prince'
);

-- Затем через delete удаляем сотрудника 
DELETE FROM Employees WHERE LastName = 'Prince';

-- 6. Проверяем изменения анологично пункту 2
SELECT * FROM Employees ORDER BY EmployeeID;