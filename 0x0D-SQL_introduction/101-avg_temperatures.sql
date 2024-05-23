-- retrives average tempratures ordered by temprature
SELECT city, AVG(tempratures) AS avg_temp from tempratures GROUP BY city  ORDER BY avg_temp;
