-- Import in hbtn_0c_0 database this table dump
--  a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
Select name, value AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
ORDER BY avg_temp DESC
LIMIT 3
