SELECT
    ROUND(AVG(machine_failure::numeric) * 100, 2) AS failure_rate_percent
FROM maintenance_raw;

SELECT
    type,
    COUNT(*) AS total_count,
    SUM(machine_failure) AS failure_count,
    ROUND(AVG(machine_failure::numeric) * 100, 2) AS failure_rate_percent
FROM maintenance_raw
GROUP BY type
ORDER BY failure_rate_percent DESC;

SELECT
    SUM(twf) AS tool_wear_failures,
    SUM(hdf) AS heat_dissipation_failures,
    SUM(pwf) AS power_failures,
    SUM(osf) AS overstrain_failures,
    SUM(rnf) AS random_failures
FROM maintenance_raw;

SELECT
    CASE
        WHEN tool_wear_min < 50 THEN 'under_50'
        WHEN tool_wear_min < 100 THEN '50_99'
        WHEN tool_wear_min < 150 THEN '100_149'
        ELSE '150_plus'
    END AS tool_wear_group,
    COUNT(*) AS total_count,
    SUM(machine_failure) AS failure_count,
    ROUND(AVG(machine_failure::numeric) * 100, 2) AS failure_rate_percent
FROM maintenance_raw
GROUP BY tool_wear_group
ORDER BY tool_wear_group;

SELECT
    CASE
        WHEN torque_nm < 20 THEN 'under_20'
        WHEN torque_nm < 40 THEN '20_39'
        WHEN torque_nm < 60 THEN '40_59'
        ELSE '60_plus'
    END AS torque_group,
    COUNT(*) AS total_count,
    SUM(machine_failure) AS failure_count,
    ROUND(AVG(machine_failure::numeric) * 100, 2) AS failure_rate_percent
FROM maintenance_raw
GROUP BY torque_group
ORDER BY torque_group;