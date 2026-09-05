-- ====================================================================
-- ENTERPRISE TRANSACTIONAL ANALYTICS CORE QUERIES
-- Target: PostgreSQL Server Analysis for Inventory, Sales, & HR
-- ====================================================================

-- 1. WINDOW FUNCTION: Ranking top selling product categories by revenue
SELECT 
    product_category,
    region_name,
    SUM(total_sales_inr) as absolute_revenue,
    DENSE_RANK() OVER (PARTITION BY region_name ORDER BY SUM(total_sales_inr) DESC) as sales_rank
FROM sales_pipeline_table
GROUP BY product_category, region_name;

-- 2. CTE (Common Table Expression): Identifying inventory items below safety stock points
WITH LowStockInventory AS (
    SELECT 
        item_name,
        stock_quantity,
        reorder_level,
        (reorder_level - stock_quantity) as deficit_units
    FROM inventory_table
    WHERE stock_quantity < reorder_level
)
SELECT *,
       CASE 
           WHEN deficit_units > 20 THEN 'CRITICAL SUPPLY BOTTLENECK'
           ELSE 'MODERATE ALERT'
       END as alert_severity
FROM LowStockInventory
ORDER BY deficit_units DESC;

-- 3. JOIN & AGGREGATION: Tracing department productivity against upskilling hours
SELECT 
    hr.department,
    COUNT(hr.employee_id) as total_staff,
    ROUND(AVG(hr.productivity_score_pct), 2) as average_productivity_index,
    SUM(hr.training_hours_completed) as total_upskilling_hours
FROM hr_performance_table hr
GROUP BY hr.department
HAVING AVG(hr.productivity_score_pct) < 85;
