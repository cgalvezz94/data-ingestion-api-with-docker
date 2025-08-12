SELECT
  d.department,
  j.job,
  SUM(CASE WHEN strftime('%m', e.hired_date) BETWEEN '01' AND '03' THEN 1 ELSE 0 END) AS Q1,
  SUM(CASE WHEN strftime('%m', e.hired_date) BETWEEN '04' AND '06' THEN 1 ELSE 0 END) AS Q2,
  SUM(CASE WHEN strftime('%m', e.hired_date) BETWEEN '07' AND '09' THEN 1 ELSE 0 END) AS Q3,
  SUM(CASE WHEN strftime('%m', e.hired_date) BETWEEN '10' AND '12' THEN 1 ELSE 0 END) AS Q4
FROM hired_employees e
JOIN departments d ON e.department_id = d.id
JOIN jobs j ON e.job_id = j.id
WHERE strftime('%Y', e.hired_date) = '2021'
GROUP BY d.department, j.job
ORDER BY d.department, j.job;
