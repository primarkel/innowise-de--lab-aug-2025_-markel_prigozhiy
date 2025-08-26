-- 1. Увеличиваем зп всех hr сотрудников ч/з update+where 
UPDATE Employees SET Salary = Salary * 1.10 WHERE Department = 'HR';

-- 2. Обновляем department сотрудников с зп > 70к на seniorit аналогично 1
UPDATE Employees SET Department = 'Senior IT' WHERE Salary > 70000.00;

-- 3. Удаляем сотрудников без проектов ч/з not exists 
DELETE FROM Employees e WHERE NOT EXISTS (
SELECT * FROM EmployeeProjects ep WHERE ep.EmployeeID = e.EmployeeID
);

-- 4. Ч/з транзакцию вставим новый проект и назначим сотрудн ков 
BEGIN;
-- вставляем новый проект и сразу получаем его projectid
WITH new_proj AS (
INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate) 
VALUES ('Data Project', 125000.00, '2025-08-01', '2025-09-04') 
RETURNING ProjectID
)
--вставляем назначения сотрудников 
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT hw.EmployeeID, np.ProjectID, hw.HoursWorked FROM new_proj np
JOIN (VALUES (1, 50), (2, 55)) AS hw(EmployeeID, HoursWorked)
ON TRUE; 
COMMIT;
-- транзакция обеспечивает, что либо операции выполнятся вместе, либо ни одна 

