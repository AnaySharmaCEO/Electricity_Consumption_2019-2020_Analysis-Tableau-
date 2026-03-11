-- SQL analysis queries for electricity consumption
-- Database: electricity.db
-- Main table: electricity_consumption
-- Columns: id, state, region, latitude, longitude, date, usage

----------------------------------------------------------------------
-- 1. Total electricity consumption by state
----------------------------------------------------------------------
SELECT
    state,
    SUM(usage) AS total_consumption_mu
FROM electricity_consumption
GROUP BY state
ORDER BY total_consumption_mu DESC;


----------------------------------------------------------------------
-- 2. Total electricity consumption by region
-- Note: 'region' may be NULL for some rows if not populated.
----------------------------------------------------------------------
SELECT
    COALESCE(region, 'Unknown') AS region,
    SUM(usage) AS total_consumption_mu
FROM electricity_consumption
GROUP BY COALESCE(region, 'Unknown')
ORDER BY total_consumption_mu DESC;


----------------------------------------------------------------------
-- 3. Year-wise electricity consumption
----------------------------------------------------------------------
SELECT
    STRFTIME('%Y', date) AS year,
    SUM(usage) AS total_consumption_mu
FROM electricity_consumption
GROUP BY STRFTIME('%Y', date)
ORDER BY year;


----------------------------------------------------------------------
-- 4. Quarter-wise electricity consumption (calendar quarters)
----------------------------------------------------------------------
SELECT
    STRFTIME('%Y', date) AS year,
    CASE
        WHEN CAST(STRFTIME('%m', date) AS INTEGER) BETWEEN 1 AND 3  THEN 'Q1'
        WHEN CAST(STRFTIME('%m', date) AS INTEGER) BETWEEN 4 AND 6  THEN 'Q2'
        WHEN CAST(STRFTIME('%m', date) AS INTEGER) BETWEEN 7 AND 9  THEN 'Q3'
        ELSE 'Q4'
    END AS quarter,
    SUM(usage) AS total_consumption_mu
FROM electricity_consumption
GROUP BY
    STRFTIME('%Y', date),
    quarter
ORDER BY
    year,
    quarter;


----------------------------------------------------------------------
-- 5. Top 10 states by total electricity usage (2019–2020)
----------------------------------------------------------------------
SELECT
    state,
    SUM(usage) AS total_consumption_mu
FROM electricity_consumption
GROUP BY state
ORDER BY total_consumption_mu DESC
LIMIT 10;


----------------------------------------------------------------------
-- 6. Bottom 10 states by total electricity usage (2019–2020)
----------------------------------------------------------------------
SELECT
    state,
    SUM(usage) AS total_consumption_mu
FROM electricity_consumption
GROUP BY state
ORDER BY total_consumption_mu ASC
LIMIT 10;


----------------------------------------------------------------------
-- 7. Consumption before and after COVID lockdown
-- India’s first national lockdown started on 24 March 2020.
-- This query compares total and average daily usage per state
-- before and after that date.
----------------------------------------------------------------------
WITH daily_state_usage AS (
    SELECT
        state,
        DATE(date) AS day,
        SUM(usage) AS daily_usage
    FROM electricity_consumption
    GROUP BY state, DATE(date)
),
flagged AS (
    SELECT
        state,
        day,
        daily_usage,
        CASE
            WHEN day < DATE('2020-03-24') THEN 'Before Lockdown'
            ELSE 'After Lockdown'
        END AS period
    FROM daily_state_usage
)
SELECT
    state,
    period,
    SUM(daily_usage) AS total_consumption_mu,
    AVG(daily_usage) AS avg_daily_consumption_mu,
    COUNT(*) AS days_counted
FROM flagged
GROUP BY state, period
ORDER BY state, period;

