Window functions in SQL, particularly in BigQuery, are powerful tools for performing calculations across a set of table rows that are related to the current row. They are often used for tasks like ranking, running totals, moving averages, and more. Here are some SQL problems that involve window functions in BigQuery:
Window functions in BigQuery are powerful tools that allow you to perform calculations across a set of table rows that are somehow related to the current row. They are particularly useful for tasks such as ranking, calculating running totals, moving averages, and other cumulative or analytic operations.

### Key Concepts of Window Functions

1. **Window Function Syntax:**
   A window function is defined using the `OVER` clause. The basic syntax is:
   ```sql
   <window_function>() OVER (
     [PARTITION BY <expression>]
     [ORDER BY <expression>]
     [window_frame]
   )
   ```

2. **Components:**
   - **PARTITION BY:** Divides the result set into partitions to which the window function is applied. Similar to `GROUP BY`, but does not reduce the number of rows.
   - **ORDER BY:** Specifies the order of rows within each partition.
   - **Window Frame:** Defines a subset of rows within the partition to perform calculations. Common frames include `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.

3. **Common Window Functions:**
   - **Aggregate Functions:** `SUM()`, `AVG()`, `COUNT()`, `MIN()`, `MAX()`
   - **Ranking Functions:** `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`
   - **Value Functions:** `LAG()`, `LEAD()`, `FIRST_VALUE()`, `LAST_VALUE()`

### Examples of Window Functions in BigQuery

#### Example 1: Running Total

Calculate a running total of sales amounts ordered by date.

```sql
SELECT
  order_id,
  order_date,
  amount,
  SUM(amount) OVER (ORDER BY order_date) AS running_total
FROM
  sales
ORDER BY
  order_date;
```

#### Example 2: Rank Products by Sales

Rank products based on their total sales amount for each day.

```sql
SELECT
  product_id,
  sale_date,
  sales_amount,
  RANK() OVER (PARTITION BY sale_date ORDER BY sales_amount DESC) AS rank
FROM
  product_sales
ORDER BY
  sale_date, rank;
```

#### Example 3: Moving Average

Calculate a 7-day moving average of sales amounts.

```sql
SELECT
  date,
  sales_amount,
  AVG(sales_amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg
FROM
  daily_sales
ORDER BY
  date;
```

#### Example 4: Lead and Lag

Compare current day sales with the previous day and the next day.

```sql
SELECT
  date,
  sales_amount,
  LAG(sales_amount, 1) OVER (ORDER BY date) AS previous_day_sales,
  LEAD(sales_amount, 1) OVER (ORDER BY date) AS next_day_sales
FROM
  daily_sales
ORDER BY
  date;
```

#### Example 5: Dense Rank for Top Performers

Identify the top 3 employees by sales performance.

```sql
SELECT
  employee_id,
  SUM(sales_amount) AS total_sales,
  DENSE_RANK() OVER (ORDER BY SUM(sales_amount) DESC) AS sales_rank
FROM
  employee_sales
GROUP BY
  employee_id
HAVING
  sales_rank <= 3;
```

### Explanation

- **Running Total:** Uses `SUM()` to compute a cumulative sum.
- **Rank Products:** Uses `RANK()` to assign ranks based on sales within each day.
- **Moving Average:** Uses `AVG()` with a frame to calculate the average over a specified range of rows.
- **Lead and Lag:** `LAG()` and `LEAD()` access data from preceding and following rows.
- **Dense Rank:** `DENSE_RANK()` assigns ranks without gaps between rank values.

Window functions in BigQuery are versatile and can be tailored to solve complex analytical challenges by leveraging the power of SQL. They enable sophisticated data analysis directly within your SQL queries, making them an essential tool for data engineers and analysts.
### Problem 1: Calculate Running Total of Sales
**Scenario:** You have a table `sales` with columns `order_id`, `order_date`, and `amount`. You want to calculate a running total of sales amounts, ordered by `order_date`.

**SQL Query:**
```sql
SELECT
  order_id,
  order_date,
  amount,
  SUM(amount) OVER (ORDER BY order_date) AS running_total
FROM
  sales
ORDER BY
  order_date;
```

### Problem 2: Rank Products by Sales
**Scenario:** You have a table `product_sales` with columns `product_id`, `sale_date`, and `sales_amount`. You want to rank the products based on their total sales amount for each day.

**SQL Query:**
```sql
SELECT
  product_id,
  sale_date,
  sales_amount,
  RANK() OVER (PARTITION BY sale_date ORDER BY sales_amount DESC) AS rank
FROM
  product_sales
ORDER BY
  sale_date, rank;
```

### Problem 3: Calculate Moving Average of Sales
**Scenario:** You have a table `daily_sales` with columns `date` and `sales_amount`. You want to calculate a 7-day moving average of the sales amounts.

**SQL Query:**
```sql
SELECT
  date,
  sales_amount,
  AVG(sales_amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg
FROM
  daily_sales
ORDER BY
  date;
```

### Problem 4: Find Top N Customers by Total Purchase
**Scenario:** You have a table `customer_orders` with columns `customer_id`, `order_id`, and `purchase_amount`. You want to find the top 3 customers by total purchase amount.

**SQL Query:**
```sql
SELECT
  customer_id,
  SUM(purchase_amount) AS total_purchase,
  RANK() OVER (ORDER BY SUM(purchase_amount) DESC) AS customer_rank
FROM
  customer_orders
GROUP BY
  customer_id
HAVING
  customer_rank <= 3;
```

### Problem 5: Identify Consecutive Days of Increased Sales
**Scenario:** You have a table `daily_sales` with columns `date` and `sales_amount`. Identify periods of consecutive days where sales increased compared to the previous day.

**SQL Query:**
```sql
WITH sales_diff AS (
  SELECT
    date,
    sales_amount,
    LAG(sales_amount) OVER (ORDER BY date) AS prev_sales_amount
  FROM
    daily_sales
),
increasing_sales AS (
  SELECT
    date,
    sales_amount,
    prev_sales_amount,
    CASE
      WHEN sales_amount > prev_sales_amount THEN 1 ELSE 0
    END AS increased
  FROM
    sales_diff
)
SELECT
  date,
  sales_amount
FROM
  increasing_sales
WHERE
  increased = 1;
```

### Explanation:
- **Running Total:** Uses `SUM()` with an `OVER` clause to calculate the cumulative sum.
- **Rank:** Uses `RANK()` with `PARTITION BY` to rank products within each partition (day).
- **Moving Average:** Uses `AVG()` with a `ROWS BETWEEN` clause to compute the moving average.
- **Top N Customers:** Uses `RANK()` to find the top customers by total purchase.
- **Consecutive Increases:** Uses `LAG()` to compare current and previous sales amounts, identifying increases.

These examples demonstrate how window functions can be used to solve various analytical problems in SQL, especially within the context of BigQuery.