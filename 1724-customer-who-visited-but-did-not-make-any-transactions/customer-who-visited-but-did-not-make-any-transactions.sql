# Write your MySQL query statement below


SELECT Visits.customer_id AS customer_id, COUNT(Visits.customer_id) AS count_no_trans
FROM Visits
WHERE Visits.visit_id NOT IN (
    SELECT Transactions.visit_id
    FROM Transactions
)
GROUP BY Visits.customer_id;