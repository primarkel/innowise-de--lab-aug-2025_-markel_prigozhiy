-- 1. Создаем нового пользовтеля через create с паролем 
CREATE ROLE hr_user LOGIN PASSWORD '12345';

-- 2. Ч/з grant даем права на select в табл. employyes
GRANT SELECT ON Employees TO hr_user;

-- 3. Аналогично даем права на insert и update 
GRANT INSERT, UPDATE ON Employees TO hr_user;