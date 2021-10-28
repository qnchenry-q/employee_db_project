CREATE DATABASE WarioINC;
GO

USE WarioINC;

--forgot to add primary key in creation
ALTER TABLE dbo.employees
ADD PRIMARY KEY (employee_id);

--The full data for each Employee with their address as a string, department name, and manager name
SELECT
    e.employee_id,
    e.name,
    e.salary,
    e.department_id,
    d.department_name,
    e.address_id,
    a.street + ' ' + a.city + ' ' + a.state 'address',
    e.manager_id,
    (
        SELECT name FROM dbo.employees WHERE employee_id = e.manager_id
    ) AS 'manager_name'

FROM
    dbo.employees e
    LEFT JOIN dbo.departments d ON e.department_id = d.department_id
    LEFT JOIN dbo.addresses a ON e.address_id =  a.address_id;
GO

--the 5 highest paid and lowest paid employees
WITH A AS (SELECT TOP 5
                    name,
                    salary
                FROM
                    dbo.employees
                ORDER BY salary ASC),
     B AS ( SELECT TOP 5
                name,
                salary
            FROM
                dbo.employees
            ORDER BY salary DESC)
SELECT
    B.name 'Top 5 salaries', 
    B.salary,
    A.name 'Bottom 5 salaries',
    A.salary
FROM B FULL OUTER JOIN A ON A.name = B.name;


--The total salary for each department, the manager's name, sorted by highest total
WITH totals AS (
                SELECT 
                    department_id,
                    SUM(salary) 'total salary'
                FROM
                    dbo.employees
                GROUP BY
                    department_id
                ),
    merged AS (
                SELECT
                    department_name,
                    d.manager_id,
                    d.department_id,
                    e.name
                FROM
                    dbo.departments d LEFT JOIN dbo.employees e ON d.manager_id = e.employee_id

    )

SELECT
    department_name,
    name 'manager name',
    [total salary]
FROM
    totals t LEFT JOIN merged m ON t.department_id = m.department_id
ORDER BY
    [total salary] DESC;
    
--Each employee that lives in a given state (The state can be hard coded for now)
SELECT 
    employee_id,
    name,
    state
FROM
    dbo.employees e LEFT JOIN dbo.addresses a ON e.address_id = a.address_id
ORDER BY
    state;