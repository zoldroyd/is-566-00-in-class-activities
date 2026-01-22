-- These commands should be run from duckdb CLI
COPY (
  SELECT * FROM read_csv_auto('orders_demo.csv')
) TO 'orders_demo.parquet'
(FORMAT PARQUET, ROW_GROUP_SIZE 5000);


-- let's look at the metadata embedded in the parquet format
SELECT
  row_group_id,
  path_in_schema AS column_name,
  stats_min_value,
  stats_max_value,
  num_values,
  total_compressed_size
FROM parquet_metadata('orders_demo.parquet')
WHERE path_in_schema IN ('country', 'order_id')
ORDER BY row_group_id, path_in_schema;



EXPLAIN ANALYZE
SELECT SUM(sales_amount)
FROM 'orders_demo.parquet'
WHERE country = 'USA';


EXPLAIN ANALYZE
SELECT SUM(sales_amount)
FROM 'orders_demo.parquet';