SELECT country,
COUNT(*) AS count
FROM Customers
GROUP BY country
ORDER BY count DESC;
