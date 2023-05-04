SELECT * FROM companies

SELECT name,city,category_code from companies

SELECT name AS company_name FROM companies

SELECT name AS company_name,city as City,category_code from companies

#Write a Query that renames all columns such that first and last letters are captialized

SELECT * FROM companies LIMIT 20

SELECT *  FROM companies
 WHERE STATUS = 'operating'

##Did any company recieve funding greatory than 10,000,000 

## Find where funding_total is NULL
SELECT *  FROM companies
 WHERE funding_total_usd IS NULL


## Find where funding_total is NULL
SELECT *  FROM companies
 WHERE name > 'a'

SELECT funding_total_usd*69.09 as FUNDIG_INR  FROM companies

## Create a new column called Region ID 
SELECT country_code || "/" || city as 'Region ID' FROM companies

## SELECT names which have fox inside
SELECT * FROM Companies WHERE name like '%Fox%'

##Find companies which have a .in domain
SELECT * FROM companies where homepage_url like "%.in"
## Find company names that have second character as a
SELECT * FROM companies where name like "_a%"

SELECT * FROM companies where name in ('8868','0-6.com')

## ORDER COMPANIES BY TOTOAL FUNDING AMOUNT. 
##Hint: Don't show NULL VALUES
SELECT * FROM companies WHERE funding_total_usd IS NOT NULL
ORDER BY funding_total_usd DESC

## Multiple Col Ordering
SELECT * FROM companies WHERE category_code IS NOT NULL
ORDER BY category_code, funding_total_usd DESC


SELECT COUNT(*) FROM companies WHERE funding_total_usd > 100000
## Count has lower value, since some are NULL
SELECT COUNT(homepage_url) FROM companies WHERE funding_total_usd > 100000

## Find number of catgories
SELECT COUNT(DISTINCT category_code) AS "Dist Cat" 
From companies WHERE category_code IS NOT NULL

##Find Total Funding received in SF Bay

SELECT SUM(funding_total_usd)  AS "Funding Total"
From companies WHERE region = "SF Bay"