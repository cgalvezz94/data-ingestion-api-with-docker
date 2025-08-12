WITH hires_per_department AS (
  SELECT
    d.id,
    d.department,
    COUNT(e.id) AS hired
  FROM hired_employees e
  JOIN departments d ON e.department_id = d.id
  WHERE strftime('%Y', e.hired_date) = '2021'
  GROUP BY d.id, d.department
),
avg_hires AS (
  SELECT AVG(hired) AS average_hires FROM hires_per_department
)
SELECT
  id,
  department,
  hired
FROM hires_per_department, avg_hires
WHERE hired > average_hires
ORDER BY hired DESC;
