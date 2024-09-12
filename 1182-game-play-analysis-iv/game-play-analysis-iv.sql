# Write your MySQL query statement below
SELECT  
       ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
       
FROM Activity 
WHERE (player_id, event_date) IN
    (SELECT player_id, DATE_ADD(MIN(event_date), INTERVAL 1 DAY)
     FROM Activity
     GROUP BY player_id)
    
;
/*
SELECT ROUND(COUNT(DISTINCT a2.player_id)/COUNT(DISTINCT a1.player_id),2) AS fraction FROM
Activity a1
LEFT JOIN ACtivity a2
ON 
a1.player_id = a2.player_id

AND a1.event_date = a2.event_date + INTERVAL 1 DAY*/

