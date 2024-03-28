-- Finds the average temperature of a city
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city;
