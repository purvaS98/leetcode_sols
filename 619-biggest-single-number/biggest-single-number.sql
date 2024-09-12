# Write your MySQL query statement below
SELECT MAX(DISTINCT(num)) AS num
FROM MyNumbers
WHERE NUM IN (
    SELECT num FROM MyNumbers
    GROUP BY NUM
    HAVING COUNT(num) = 1
);


