SELECT COUNT(*) AS total_rows
FROM maintenance_raw;

SELECT *
FROM maintenance_raw
LIMIT 5;

SELECT
    type,
    COUNT(*) AS cnt
FROM maintenance_raw
GROUP BY type
ORDER BY cnt DESC;