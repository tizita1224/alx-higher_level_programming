-- lists all number of records with the same score
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
