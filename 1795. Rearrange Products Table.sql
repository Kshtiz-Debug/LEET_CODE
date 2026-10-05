---Table: Products

--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| product_id  | int     |
--| store1      | int     |
--| store2      | int     |
--| store3      | int     |
--+-------------+---------+
--product_id is the primary key (column with unique values) for this table.
--Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
--If the product is not available in a store, the price will be null in that store's column.
 

--Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

--Return the result table in any order.

--The result format is in the following example.
---

-- Write your PostgreSQL query statement below
select product_id , 'store1' as store , store1 as price
from Products 
where store1 is not null

union all

select product_id , 'store2' as store , store2 as price
from Products 
where store2 is not null


union all



select product_id , 'store3' as store , store3 as price
from Products 
where store3 is not null




-- with no doubts this way is a really good way to solve this problem but its not the best one 
-- instead of this what u can do is to use Values in this wait lateral join 
-- this is supposedly a new topic for me now , ill learn it n add the solution to it soon 
