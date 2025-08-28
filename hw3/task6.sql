SELECT item,
COUNT(*) AS total_orders, ROUND(AVG(amount), 2) AS avg_amount
FROM Orders
GROUP BY item
ORDER BY total_orders DESC;
