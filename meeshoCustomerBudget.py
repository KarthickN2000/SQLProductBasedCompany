
#find how many products falls into customer budget along with the list of products
#Incase of clash choose the less costly products

create table products
(
product_id varchar(20) ,
cost int
);
insert into products values ('P1',200),('P2',300),('P3',500),('P4',800);

create table customer_budget
(
customer_id int,
budget int
);

insert into customer_budget values (100,400),(200,800),(300,1500);


#MYSQL QUERY


with moving_sum_cte as(
SELECT product_id,
  SUM(cost) OVER (
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS moving_sum
FROM product_s)

select cb.customer_id,group_concat(msc.product_id) from customer_budget cb
join moving_sum_cte msc
on cb.budget >= msc.moving_sum
group by cb.customer_id;



#output

300	P1,P2,P3
200	P1,P2
100	P1
