# Write your MySQL query statement below
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
    SELECT product_id, min(year) FROM Sales
    GROUP BY product_id
);
/*
Below doesnt work because if we select the min year then the quantity and price are not for that year but the first record of the product_id
SELECT product_id, MIN(year) AS first_year, quantity, price
FROM Sales
GROUP BY product_id
*/