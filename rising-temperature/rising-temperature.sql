# Write your MySQL query statement below
WITH weatherStat AS
    (SELECT
        id,
        temperature - LAG(temperature) OVER (ORDER BY recordDate) AS temp_diff,
        DATEDIFF(recordDate, LAG(recordDate) OVER (ORDER BY recordDate)) AS date_diff
    FROM
        weather)
        

SELECT
    id
FROM
    weatherStat
WHERE
    temp_diff > 0 AND 
    date_diff = 1