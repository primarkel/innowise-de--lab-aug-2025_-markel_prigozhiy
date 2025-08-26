-- 1. Пишем функцию для бонуса сотрудникам ч/з function 
CREATE OR REPLACE FUNCTION CalculateAnnualBonus(emp_id INT, emp_salary NUMERIC)
RETURNS NUMERIC AS $$
BEGIN 
RETURN emp_salary * 0.10;
END; 
$$ LANGUAGE plpgsql; -- plpgsql потому что begin end; $$ как рамки 

-- 2. Выбираем бонус для сотрудников 
SELECT EmployeeID, FirstName, LastName, Salary, CalculateAnnualBonus(EmployeeID, Salary) 
AS BONUS FROM Employees;

-- 3. Создадим представление view по сотрудника отдела 
CREATE OR REPLACE VIEW IT_Department_View AS 
SELECT EmployeeID, FirstName, LastName, Salary 
FROM Employees WHERE Department = 'IT';

-- 4. Проверяем представление 
SELECT * FROM IT_Department_View;

