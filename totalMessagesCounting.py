#find the total messages between each person on a single day

CREATE TABLE subscriber (
 sms_date date ,
 sender varchar(20) ,
 receiver varchar(20) ,
 sms_no int
);

-- insert some values
INSERT INTO subscriber VALUES ('2020-4-1', 'Avinash', 'Vibhor',10);
INSERT INTO subscriber VALUES ('2020-4-1', 'Vibhor', 'Avinash',20);
INSERT INTO subscriber VALUES ('2020-4-1', 'Avinash', 'Pawan',30);
INSERT INTO subscriber VALUES ('2020-4-1', 'Pawan', 'Avinash',20);
INSERT INTO subscriber VALUES ('2020-4-1', 'Vibhor', 'Pawan',5);
INSERT INTO subscriber VALUES ('2020-4-1', 'Pawan', 'Vibhor',8);
INSERT INTO subscriber VALUES ('2020-4-1', 'Vibhor', 'Deepak',50);


#MYSQL query

#String comparison

select sms_date,sender,receiver,sum(sms_no) as total_messages from(select sms_date,
case when sender < receiver then sender else receiver end as sender,
case when sender > receiver then sender else receiver end as receiver,
sms_no
from subscriber) a
group by sms_date,sender,receiver


#output

2020-04-01	Avinash	Vibhor	30
2020-04-01	Avinash	Pawan	50
2020-04-01	Pawan	Vibhor	13
2020-04-01	Deepak	Vibhor	50
