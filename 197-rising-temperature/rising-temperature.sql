# Write your MySQL query statement below
SELECT temp1.id

FROM Weather AS temp1


JOIN Weather AS temp2 ON temp1.recordDate = temp2.recordDate + INTERVAL 1 DAY
WHERE temp1.temperature > temp2.temperature;