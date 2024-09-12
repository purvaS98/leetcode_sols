# Write your MySQL query statement below

/* With Subquery
SELECT Visits.customer_id AS customer_id, COUNT(Visits.customer_id) AS count_no_trans
FROM Visits
WHERE Visits.visit_id NOT IN (
    SELECT Transactions.visit_id
    FROM Transactions
)
GROUP BY Visits.customer_id;*/

SELECT v.customer_id, COUNT(v.customer_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id
