SELECT * FROM companies WHERE "status"="operating"

SELECT * FROM companies LIMIT 5

SELECT usd_funding FROM companies

SELECT * FROM companies WHERE funcding_status < 5000

SELECT * FROM companies WHERE funcding_status IS NULL

SELECT * FROM companies WHERE funcding_status IS NOT NULL

SELECT regions || "/" ||| city AS "Region/CITY" from companies

 SELECT * FROM companies WHERE name LIKE "%Fox%" ##everithing that contains fox

SELECT * FROM companies WHERE name LIKE ".%"  ##everything that start with the dot

SELECT * FROM companies WHERE funcding_status IS NOT NULL
ORDER BY funcdy_total_usd DESC
LIMIT 5

SELECT SUM(funding_total_usd) AS "Funding total"
FROM companies
WHERE region="SF Bay"

LIKE, IN, BETWEEN, IS NULL, AND, OR, NOT

SELECT DINSTINCT cathegories AS "Dist Cathegories"
WHERE cathegory_code IS NOT null

SELECT COUNT(DINSTINCT cathegories) AS "Dist Cathegories"
WHERE cathegory_code IS NOT null

 select ROUND(AVG(COALESCE(funcdy_total_usd, 0), 2)) AS "AVG Funding"  ###COALESCE permet de remplacer NULL par kke chose
 FROM companies

 SELECT strftime("%Y", founded_at) FROM companies ##give  all in year from 2020-23-2

 /*find count companies founded each year*/
SELECT strftime("%Y", founded_at) as year_founded
COUNT(founded_at) as count_companies
FROM companies
GROUP BY founded_at
ORDER BY 2 DESC

--
SELECT strftime("%Y", founded_at) as year_founded
COUNT(founded_at) as count_companies
FROM companies
GROUP BY founded_at
HAVING count_companies > 10
ORDER BY 2 DESC

--count number of acquisitions made by each company with two tables
SELECT name, COUNT(companies_name) FROM companies
JOIN acquisitions ON permalink = acquire_permalink
GROUP BY name




  



 